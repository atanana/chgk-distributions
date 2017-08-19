var socket = io.connect('http://' + document.domain + ':' + location.port);
var assertImg = document.getElementById('asset');

socket.on('asset change', function (data) {
    assertImg.src = '/static/assets/' + data.name;
});
