const socket = io(); //'http://127.0.0.1:5000');

socket.on("connect", () => {
    console.log(socket.id); // x8WIv7-mJelg7on_ALbx
  });
  
document.getElementById('join-btn').
addEventListener('click', function(event) {
    event.preventDefault();
    console.log('clicked')
    socket.emit('user_joined', {
        'name': document.getElementById('name').value,
        'room': document.getElementById('room').value
    });
});