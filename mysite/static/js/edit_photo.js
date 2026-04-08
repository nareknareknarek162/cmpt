const form = document.querySelector("form");

function populatePhoto(photoId) {
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
            document.getElementById("photo-title").value = data.title;
            document.getElementById("photo-description").value = data.description;
            document.getElementById("photo-preview").src = data.image;
            document.getElementById("photo-image").removeAttribute("required");

        })
        .catch(error => {
            console.error(error);
        });
}

function updatePhoto(photoId) {
    const apiURL = `http://127.0.0.1:8000/api/photo/${photoId}/`;
    let access_token = localStorage.getItem("access_token");

    const photoData = new FormData();
    photoData.append("title", document.getElementById("photo-title").value);
    photoData.append("description", document.getElementById("photo-description").value);
    if (document.getElementById("photo-image").files[0]) {
    photoData.append("image", document.getElementById("photo-image").files[0]);

    }
    fetch(apiURL, {method: "PATCH",
        headers: {"Accept": "application/json",
                "Authorization": `Bearer ${access_token}`},
        body: photoData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            //
        })
        .catch(error => {

        });
}

const pathParts = window.location.pathname.split('/');
const photoId = pathParts[pathParts.length - 2];
populatePhoto(photoId);

form.addEventListener('submit', (event) => {
    event.preventDefault();
    updatePhoto(photoId);
});
