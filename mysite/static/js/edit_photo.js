function populatePhoto(photoId) {
    const apiURL = `http://127.0.0.1:8000/api/photo/${photoId}/`;
    let access_token = localStorage.getItem("access_token");

    fetch(apiURL, {
            method: "GET",
            headers: {"Accept": "application/json",
                "Authorization": `Bearer ${access_token}`},
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
            document.getElementById("photo-preview").src = data.image_detail;
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
            window.location.replace('http://127.0.0.1:8000/account/');
        })
        .catch(error => {

        });
}

const form = document.querySelector("form");
const photoId = window.location.pathname.split('/').slice(-2, -1)[0];

populatePhoto(photoId);

form.addEventListener('submit', (event) => {
    event.preventDefault();
    updatePhoto(photoId);
});

document.getElementById('photo-image').addEventListener('change', function() {
    const file = this.files[0];
    const errorDiv = document.getElementById('image-error');
    const submitBtn = document.querySelector('button[type="submit"]');

    if (file && !file.type.startsWith('image/')) {
        this.classList.add('is-invalid');
        errorDiv.style.display = 'block';


        this.value = '';
    } else {
        this.classList.remove('is-invalid');
        this.classList.add('is-valid');
        errorDiv.style.display = 'none';
    }
});
