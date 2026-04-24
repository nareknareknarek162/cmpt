const username = localStorage.getItem("username");

function fetchPhoto() {
    const photoId = window.location.pathname.split("/")[2];
    const apiURL = `http://127.0.0.1:8000/api/photo/${photoId}/`;
    let access_token = localStorage.getItem("access_token");
    const headers = {
        "Content-Type": "application/json",
        ...(access_token && {
            "Authorization": `Bearer ${access_token}`
        })
    };


    fetch(apiURL, {
            method: "GET",
            headers
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
            <img src="${data.image_detail}" class="rounded mx-auto d-block">
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

    let access_token = localStorage.getItem("access_token");
    const headers = {
        "Content-Type": "application/json",
        ...(access_token && {
            "Authorization": `Bearer ${access_token}`
        })
    };

    fetch(apiURL, {
            method: "GET",
            headers
        })
        .then(response => {
            return response.json();
        })
        .then(data => {

            document.getElementById("likes-count").textContent = data["likes"].length;

            if (data["liked"]) {
                const button = document.getElementById("like_button");
                button.innerHTML = "Убрать лайк";
                button.dataset.method = "DELETE"
            }


        })
        .catch(error => {
            console.error(error);
        });
}

function toggleLike() {
    const id = window.location.pathname.split("/")[2];
    const apiURL = `http://127.0.0.1:8000/api/like/photo/${id}/`;

    const button = document.getElementById("like_button");
    httpMethod = button.dataset.method

    let access_token = localStorage.getItem("access_token");
    fetch(apiURL, {
            method: httpMethod,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access_token}`
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
        })
        .then(data => {
            const el = document.getElementById("likes-count");
            if (httpMethod == "POST") {
                button.innerHTML = "Убрать лайк";
                button.dataset.method = "DELETE";
                el.textContent = Number(el.textContent) + 1;
            }
            if (httpMethod == "DELETE") {
                button.innerHTML = "Лайкнуть";
                button.dataset.method = "POST";
                el.textContent = Number(el.textContent) - 1;
            }

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
            const isAuthor = comment.author === username;

            const dropdown = isAuthor ? ` <div class="dropdown position-absolute top-0 end-0 m-2">
              <button class="btn btn-sm text-muted p-0" data-bs-toggle="dropdown" style="width: 32px; height: 32px;">
                <i class="bi bi-three-dots-vertical fs-5"></i>
              </button>
              <ul class="dropdown-menu dropdown-menu-end">
                <li>
                  <button class="dropdown-item edit-comment" data-id="${comment.id}" data-bs-toggle="modal" data-bs-target="#myModal"> Редактировать </button>
                </li>
                <li>
                  <button class="dropdown-item text-danger delete-comment" data-id="${comment.id}"> Удалить </button>
                </li>
              </ul>
            </div> ` : "";

            html += `
            <div class="card mb-1 mt-2" id="${comment.id}">
                <div class="card-body position-relative pe-5">

                    ${dropdown}

                    <h6 class="card-subtitle mb-1 text-muted">
                        ${comment.author} | ${comment.created_at}
                    </h6>

                    <p class="card-text">${comment.text}</p>

                </div>

                <div class="d-flex justify-content-end">
                    <button class="btn text-muted p-0 reply-comment"
                        data-id="${comment.id}"
                        data-bs-target="#myModal"
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
});


const logoutBtn = document.getElementById("logoutBtn");
const sendCommentBtn = document.getElementById("sendCommentBtn");

if (username) {
    const container = document.getElementById("authentication");

    container.innerHTML = `
    <button type="submit" class="btn btn-danger" id="logoutBtn">Выйти</button>
    <a href="/account/" class="me-3">
        <button class="btn btn-primary">Личный кабинет</button>
    </a>
    <div class="border-start ps-3 fs-5 text-success">
        ${username}
    </div>`;
}

if (sendCommentBtn) {
    sendCommentBtn.addEventListener("click", sendComment);
}

document.addEventListener('click', (event) => {

    if (event.target.matches('#logoutBtn')) {

        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        localStorage.removeItem("username");

        const container = document.getElementById("authentication");
        container.innerHTML = `
            <a href="/auth/" class="me-2">
                <button class="btn btn-primary">Войти</button>
            </a>
            <a href="/registration/">
                <button class="btn btn-secondary">Зарегистрироваться</button>
            </a>`;
    }
    if (event.target.matches('.delete-comment')) {
        const photoId = event.target.dataset.id;
        deletePhoto(photoId);
    }
    if (event.target.matches("#like_button")) {
        if (username) {
            toggleLike();
        }

    }
});

const tooltipList = (!username &&
    [...document.querySelectorAll('[data-bs-toggle="tooltip"]')]
        .map(el => {
            el.setAttribute('title', 'Войдите, чтобы лайкать фотографии');
            return new bootstrap.Tooltip(el);
        })
) || [];
