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

form.addEventListener('submit', (event) => {
    event.preventDefault();
});

const pathParts = window.location.pathname.split('/');
const photoId = pathParts[pathParts.length - 2];
populatePhoto(photoId);
