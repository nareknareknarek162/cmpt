let access_token = localStorage.getItem("access_token");
if (access_token) {
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";

    const socket = new WebSocket(
    `${protocol}//${window.location.host}/ws/notifications/?token=${access_token}`);

    function showNotification(message) {
        const toastElement = document.createElement("div");

        toastElement.className =
            "toast align-items-center text-bg-dark border-0 mb-2";

        toastElement.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>

            <button
                type="button"
                class="btn-close btn-close-white me-2 m-auto"
                data-bs-dismiss="toast">
            </button>
        </div>
    `;

        document
            .getElementById("toast-container")
            .appendChild(toastElement);

        const toast = new bootstrap.Toast(toastElement, {
            delay: 4000
        });

        toast.show();

        toastElement.addEventListener("hidden.bs.toast", () => {
            toastElement.remove();
        });
    }

    socket.onmessage = function (event) {

        showNotification(event.data);
    };

    document.getElementById("logoutBtn").addEventListener("click", function () {
        socket.close();
    });
}
