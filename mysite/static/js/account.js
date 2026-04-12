const select = document.getElementById("state");
const username = localStorage.getItem("username");

function fetchPhotos(state="approved") {
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

    const modify =
        state === "on_delete" ?
        `<a href="/photo/restore/${photo.id}" class="dropdown-item">
             Восстановить
           </a>` :
        `<a href="/photos/edit/${photo.id}" class="dropdown-item">
             Редактировать
           </a>`;

    const html = `
         <div class="col-6 col-md-4 mb-3">
          <div class="position-relative d-inline-block" id="${photo.id}">
            <a href="http://127.0.0.1:8000/photo/${photo.id}/">
            <img src="${photo.image_preview}"
                 title="${photo.description}"
                 class="img-fluid rounded">
            </a>
            <div class="dropdown position-absolute top-0 end-0">
              <button class="btn btn-sm btn-light" data-bs-toggle="dropdown">
                <i class="bi bi-three-dots-vertical fs-8"></i>
              </button>
              <ul class="dropdown-menu">
                <li>${modify}</li>
                <li>
                  <button class="dropdown-item delete-btn text-danger"
                          data-id="${photo.id}">
                    Удалить
                  </button>
                </li>
              </ul>
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
    .then(data => {
        const element = document.getElementById(`${photoId}`);
        element.remove();
    })
    .catch(error => {
        console.error(error);
    });
}

if (username) {
    const container = document.getElementById("username");
    container.innerHTML = `${username}`;
}

document.addEventListener("DOMContentLoaded", () => {
    fetchPhotos();
});

document.addEventListener('click', (event) => {
  if (event.target.matches('.delete-btn')) {
    const photoId = event.target.dataset.id;
    deletePhoto(photoId);
  }
});

select.addEventListener("change", (e) => {
    const status = e.target.value;
    fetchPhotos(status);
});
