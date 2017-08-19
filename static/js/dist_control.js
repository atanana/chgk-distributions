var socket = io.connect('http://' + document.domain + ':' + location.port);

var onChange = function (event) {
    socket.emit('asset select', {name: event.target.value});
};

document.querySelectorAll('input[type=radio]')
    .forEach(function (input) {
        input.onchange = onChange;
    });