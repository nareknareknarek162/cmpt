export function refreshToken(refresh_token) {
const apiURL = 'http://127.0.0.1:8000/api/token/refresh/';

    fetch(apiURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"refresh": refresh_token})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            localStorage.setItem("access_token", data.access);
        });
}
