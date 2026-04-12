const username = localStorage.getItem("username");

function fetchPhotos(page=1) {
    const apiURL = 'http://127.0.0.1:8000/api/photo/';

    const form = document.getElementById("photo-form");

    const formData = new FormData(form);
    const search = formData.get('search');
    const sort = formData.get('sort');
    const order = formData.get('order');

    const params = new URLSearchParams();
    params.append("sort", sort);
    params.append("order", order);
    params.append("state", "approved");
    if (search) params.append("search", search);
    params.append("page", page);

    fetch(`${apiURL}?${params.toString()}`, {
            method: "GET"
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            return response.json();
        })
        .then(data => {

            const container = document.getElementById("photos-container");
            container.innerHTML = "";

            data["results"].forEach(photo => {

                const html = `
                <div class="col-6 col-md-4 mb-3">
                    <a href="/photo/${photo.id}/">
                        <img src="${photo.image_preview}"
                             title="${photo.description}"
                             class="img-fluid rounded">
                    </a>
                </div>
            `;

                container.innerHTML += html;
            });
            const pagination = document.getElementById("pagination");
            pagination.innerHTML = "";
            if (data.pagination.prev_page != null) {
                pagination.innerHTML += `<li class="page-item">
                                        <a class="page-link" href="#" data-page="1">&laquo;</a>
                                      </li>
                                      <li class="page-item">
                                        <a class="page-link" href="#" data-page="${data.pagination.prev_page}">Предыдущая</a>
                                      </li>`;
            }

            pagination.innerHTML += `<li class= "page-item active"><span class="page-link">${data.pagination.current_page}</span></li>`;

            if (data.pagination.next_page != null) {
                pagination.innerHTML += `<li class="page-item">
                                    <a class="page-link" href="#" data-page="${data.pagination.next_page}">Следующая</a>
                                  </li>
                                  <li class="page-item">
                                    <a class="page-link"} href="#" data-page="${data.pagination.total_pages}">&raquo;</a>
                                  </li>`;
            }

        })
        .catch(error => {
            console.error(error);
        });
}

document.addEventListener("DOMContentLoaded", () => {
    fetchPhotos();
});

document.addEventListener("submit", function(e) {
    e.preventDefault();
    fetchPhotos();
});

document.addEventListener("click", (e) => {
    const link = e.target.closest("a.page-link");
    if (!link) return;

    e.preventDefault();

    const page = link.dataset.page;

    if (page) {
        fetchPhotos(page);
    }
});

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

document.addEventListener("click", function(event) {

    if (event.target.id === "logoutBtn") {

        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        localStorage.removeItem("username");
        const container = document.getElementById("authentication").innerHTML = `<a href="/auth/" class="me-2">
                <button class="btn btn-primary">Войти</button>
            </a>
            <a href="/registration/">
                <button class="btn btn-secondary">Зарегистрироваться</button>
            </a>`;
    }

});
