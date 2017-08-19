var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function () {
    socket.emit('my event', {data: 'I\'m connected!'});
});

var onChange = function () {
    var radio = findSelectedRadio();
    if (radio) {
        console.log(radio.value)
    }
};

function findSelectedRadio() {
    var radios = findRadios();
    for (var i = 0; i < radios.length; i++) {
        var radio = radios[i];
        if (radio.checked) {
            return radio;
        }
    }
}

function findRadios() {
    return document.querySelectorAll('input[type=radio]');
}

findRadios()
    .forEach(function (input) {
        input.onchange = onChange;
    });