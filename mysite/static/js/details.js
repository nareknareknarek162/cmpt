function fetchPhoto() {
    const photoId = window.location.pathname.split("/")[2];
    const apiURL = `http://127.0.0.1:8000/api/photo/${photoId}/`;


    fetch(apiURL, {
            method: "GET"
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            return response.json();
        })
        .then(data => {

            const container = document.getElementById("photo");

            const html = `
            <p class="text-center fw-semibold fs-2">${data.title}</p>
            <img src="${data.image}" class="rounded mx-auto d-block">
            <p class="text-center">${data.description}</p>
            <p class="text-center">Автор: ${data.author}</p>
            <p class="text-center">Загружено: ${data.publication_date}</p>
            `;
            container.insertAdjacentHTML('beforeend', html);


        })
        .catch(error => {
            console.error(error);
        });
}

function fetchLikes() {
    const id = window.location.pathname.split("/")[2];
    const apiURL = `http://127.0.0.1:8000/api/like/photo/${id}/list/`;


    fetch(apiURL, {
            method: "GET"
        })
        .then(response => {
            return response.json();
        })
        .then(data => {

            const container = document.getElementById("likes");

            const html = `<p>Всего лайков ${data.length}</p>`;
            container.innerHTML = html;


        })
        .catch(error => {
            console.error(error);
        });
}

function fetchComments() {
    const id = window.location.pathname.split("/")[2];
    const apiURL = `http://127.0.0.1:8000/api/comment/photo/${id}/list/`;

    fetch(apiURL, {
            method: "GET"
        })
        .then(response => response.json())
        .then(data => {
            const commentsContainer = document.getElementById("comments");
            let html = "";

            data.forEach(comment => {
                html += `
                    <div class="card mb-1 mt-2" id="${comment.id}">
                        <div class="card-body position-relative pe-5">

                            <div class="dropdown position-absolute top-0 end-0 m-2">
                                <button
                                    class="btn btn-sm text-muted p-0"
                                    data-bs-toggle="dropdown"
                                    style="width: 32px; height: 32px;">
                                    <i class="bi bi-three-dots-vertical fs-5"></i>
                                </button>
                                <ul class="dropdown-menu dropdown-menu-end">
                                    <li>
                                        <button class="dropdown-item edit-comment" data-id="${comment.id}"
                                        data-bs-toggle="modal" data-bs-target="#myModal">
                                            Редактировать
                                        </button>
                                    </li>
                                    <li>
                                        <button class="dropdown-item text-danger delete-comment" data-id="${comment.id}">
                                            Удалить
                                        </button>
                                    </li>
                                </ul>
                            </div>

                            <h6 class="card-subtitle mb-1 text-muted">
                                ${comment.author} | ${comment.created_at}
                            </h6>

                            <p class="card-text">${comment.text}</p>

                        </div>
                        <div class="d-flex justify-content-end">
                            <button class="btn text-muted p-0 reply-comment" data-id="${comment.id}" data-bs-target="#myModal"
                            data-bs-toggle="modal">
                                <i class="bi bi-reply fs-4"></i>
                            </button>
                        </div>
                    </div>
                `;
            });

            commentsContainer.innerHTML = html;
        })
        .catch(error => console.error(error));
}

function deletePhoto(commentId) {
    const apiURL = `http://127.0.0.1:8000/api/comment/${commentId}/`;
    let access_token = localStorage.getItem("access_token");

    fetch(apiURL, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${access_token}`
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.statusText);
        }
    })
    .then(data => {
        const element = document.getElementById(`${commentId}`);
        element.remove();
    })
    .catch(error => {
        console.error(error);
    });
}

function isAuthenticated() {
    const apiURL = "http://127.0.0.1:8000/api/user/current/";
    const access_token = localStorage.getItem("access_token");

    if (access_token) {
        fetch(apiURL, {
                method: "GET",
                headers: {
                    "Authorization": "Bearer " + access_token
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(response.statusText);
                }
                return response.json();
            })
            .then(data => {

                const container = document.getElementById("authentication");

                container.innerHTML = `
                <button type="submit" class="btn btn-danger" id="logoutBtn">Выйти</button>
                <a href="{% url 'account' %}" class="me-3">
                    <button class="btn btn-primary">Личный кабинет</button>
                </a>
                <div class="border-start ps-3 fs-5 text-success">
                    ${data.username}
                </div>`;
            })
            .catch(error => {
                console.error(error);
            });
    }
}

function sendComment() {
    const photoId = window.location.pathname.split("/")[2];
    const apiURL = `http://127.0.0.1:8000/api/comment/photo/${photoId}/`;

    comment_text = document.getElementById("comment_text").value;
    let access_token = localStorage.getItem("access_token");

    fetch(apiURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access_token}`
            },
            body: JSON.stringify({
                "text": comment_text
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("success");
        })
        .catch(error => {
            console.error(error);
        });
}

document.addEventListener("DOMContentLoaded", () => {
    fetchPhoto();
    fetchLikes();
    fetchComments();
    isAuthenticated();
});


const logoutBtn = document.getElementById("logoutBtn");
const sendCommentBtn = document.getElementById("sendCommentBtn");

if (logoutBtn) {
    logoutBtn.addEventListener("click", function() {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        const container = document.getElementById("authentication");
        if (container) {
            container.innerHTML += `
                <a href="auth/" class="me-2">
                    <button class="btn btn-primary">Войти</button>
                </a>
                <a href="registration/">
                    <button class="btn btn-secondary">Зарегистрироваться</button>
                </a>`;
        }
    });
}

if (sendCommentBtn) {
    sendCommentBtn.addEventListener("click", sendComment);
}

document.addEventListener('click', (event) => {
  if (event.target.matches('.delete-comment')) {
    const photoId = event.target.dataset.id;
    deletePhoto(photoId);
  }
});
