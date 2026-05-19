let access_token = localStorage.getItem("access_token");
const socket = new WebSocket(`ws://127.0.0.1:8000/ws/notifications/?token=${access_token}`);

socket.onmessage = (event) => {
    console.log("message from server:", event.data);
    alert(event.data);
};
