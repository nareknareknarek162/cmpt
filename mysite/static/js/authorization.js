export function authorizeUser(username, password) {
    const apiURL = 'http://127.0.0.1:8000/api/token/';

    fetch(apiURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "username": username,
                "password": password
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            localStorage.setItem("access_token", data.access);
            localStorage.setItem("refresh_token", data.refresh);
            window.location.replace('http://127.0.0.1:8000/account/');
        })
        .catch(error => {
            const container = document.getElementById('dataContainer');
            container.innerHTML = `<p>Пользователь с указанными данными не найден</p>`;
            console.error('Fetch error:', error);
        });
}
if (document.getElementById('fetchButton')){
document.getElementById('fetchButton').addEventListener('click', (event) => {
    let username = document.getElementById("usernameId").value;
    let password = document.getElementById("passwordId").value;

    event.preventDefault();
    authorizeUser(username, password);
 });
}