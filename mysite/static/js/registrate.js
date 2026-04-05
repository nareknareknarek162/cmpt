function registrateUser() {
    const apiURL = 'http://127.0.0.1:8000/api/user/';
    const form = document.querySelector("form");

    const userData = Object.fromEntries(new FormData(form).entries());
    fetch(apiURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // window.location.replace('http://127.0.0.1:8000/account/');
        })
        .catch(error => console.error(error));
}

document.addEventListener('submit', (event) => {
    event.preventDefault();
    registrateUser();
 });