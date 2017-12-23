var socket = io.connect('http://' + document.domain + ':' + location.port);
var assertImg = document.getElementById('asset');

socket.on('asset change', function (data) {
    assertImg.style.display = data.name ? 'block' : 'none';
    assertImg.src = '/static/assets/' + data.name;
});
