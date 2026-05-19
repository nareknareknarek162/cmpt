import {refreshToken} from './refresh.js';

const select = document.getElementById("state");
const username = localStorage.getItem("username");

if (username) {
    const container = document.getElementById("username");
    container.innerHTML = `${username}`;
}

function fetchPhotos(state = "approved") {
    const apiURL = 'http://127.0.0.1:8000/api/photo/?mine=true';
    let access_token = localStorage.getItem("access_token");

    fetch(`${apiURL}&state=${state}`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${access_token}`
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById("photos");
            container.innerHTML = "";

            data["results"].forEach(photo => {

                const dropdown =
                    state === "on_delete" ?
                        `<ul class="dropdown-menu">
            <li>
                <button id="restoreBtn" class="dropdown-item" data-id="${photo.id}">
                    Восстановить
                </button>
            </li>
        </ul>` :
        `<ul class="dropdown-menu">
           <li>
              <a href="/photos/edit/${photo.id}" class="dropdown-item">
              Редактировать
              </a>
           </li>
           <li>
              <button class="dropdown-item delete-btn text-danger"
                 data-id="${photo.id}">
              Удалить
              </button>
           </li>
        </ul>`;

                const html = `
         <div class="col-6 col-md-4 mb-3">
          <div class="position-relative d-inline-block" id="${photo.id}">
            <a href="http://127.0.0.1:8000/photo/${photo.id}/">
            <img alt="${photo.description}" src="${photo.image_preview}"
                 title="${photo.description}"
                 class="img-fluid rounded">
            </a>
            <div class="dropdown position-absolute top-0 end-0">
              <button class="btn btn-sm btn-light" data-bs-toggle="dropdown">
                <i class="bi bi-three-dots-vertical fs-8"></i>
              </button>
               ${dropdown}
            </div>
          </div>
        </div>
        `;
                container.innerHTML += html;
            });
        })
        .catch(error => {
            console.error(error);
        });
}

function deletePhoto(photoId) {
    const apiURL = `http://127.0.0.1:8000/api/photo/${photoId}/`;
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
        .then(() => {
            const element = document.getElementById(`${photoId}`);
            element.remove();
        })
        .catch(error => {
            console.error(error);
        });
}

document.addEventListener("DOMContentLoaded", () => {
    fetchPhotos();
});

document.addEventListener('click', async (event) => {
    if (event.target.matches('.delete-btn')) {
        const photoId = event.target.dataset.id;
        deletePhoto(photoId);
    }

    if (event.target.matches('.btn-outline-secondary')) {
        const refresh_token = localStorage.getItem("refresh_token");
        refreshToken(refresh_token);

        const token = localStorage.getItem('access_token');

        try {
            await navigator.clipboard.writeText(token);
            document.getElementById('token').textContent = token;
        } catch (e) {
            console.error('Ошибка копирования', e);
        }
    }

    if (event.target.matches('#logoutBtn')) {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        localStorage.removeItem("username");

    }
    if (event.target.matches('#restoreBtn')) {
        const photoId = event.target.dataset.id;
        const apiURL = `http://127.0.0.1:8000/api/photo/${photoId}/`;
        let access_token = localStorage.getItem("access_token");

        const data = new FormData();
        data.append("restore", "true");

        fetch(apiURL, {
            method: "PATCH",
            headers: {
                "Accept": "application/json",
                "Authorization": `Bearer ${access_token}`
            },
            body: data,
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(response.statusText);
                }
            })
            .then(() => {
                const element = document.getElementById(`${photoId}`);
                element.remove();
            })
            .catch(error => {
                console.error(error);
            });

    }
});

select.addEventListener("change", (e) => {
    const status = e.target.value;
    fetchPhotos(status);
});
