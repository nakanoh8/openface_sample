// const { getDefaultSettings } = require("http2");

//動画流す準備
var video = document.getElementById('video');
// getUserMedia によるカメラ映像の取得
var media = navigator.mediaDevices.getUserMedia({ video: true });
//リアルタイムに再生（ストリーミング）させるためにビデオタグに流し込む
media.then((stream) => {
    video.srcObject = stream;
});

var canvas = document.getElementById('canvas');
canvas.setAttribute('width', video.width);
canvas.setAttribute('height', video.height);
var context = canvas.getContext('2d');

var canvas2 = document.getElementById('canvas2');
canvas2.setAttribute('width', video.width);
canvas2.setAttribute('height', video.height);
var context2 = canvas2.getContext('2d');
canvas2.strokeStyle = '#FF0000';

var img_file_name = null;

var xhr = new XMLHttpRequest();

function authenticate() {
    // context2.drawImage(video, 0, 0, video.width, video.height);
    postFaceRecog(canvas.toDataURL('image/jpeg').replace(/^.*,/, ''));
}

// video.addEventListener('timeupdate', saveCaptureImg(), true);
video.addEventListener(
    'timeupdate',
    function () {
        var canvas = document.getElementById('canvas');
        canvas.setAttribute('width', video.width);
        canvas.setAttribute('height', video.height);
        context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, video.width, video.height);
    },
    true
);

document.addEventListener('keydown', (event) => {
    var keyName = event.key;
    if (keyName === ' ') {
        console.log(`keydown: SpaceKey`);
        // authenticate();
        postTest();
        // getTest();
    }
});

function drawFaceBB() {
    postFaceBB(canvas.toDataURL('image/jpeg').replace(/^.*,/, ''));
}

function postFaceRecog(img_base64) {
    const body = new FormData();
    body.append('img', img_base64);
    xhr.open('POST', 'http://localhost:3000/face_recog', true);
    xhr.onload = () => {
        console.log(xhr.responseText)
        drawFaceBB();
    };
    xhr.send(body);
}

function postFaceBB(cap_img_base64) {
    const body = new FormData();
    body.append('img', cap_img_base64);
    xhr.open('POST', 'http://localhost:3000/face_bb', true);
    xhr.onload = () => {
        res = JSON.parse(xhr.responseText);
        context2.clearRect(0, 0, video.width, video.height);
        context2.strokeRect(res.x, res.y, res.w, res.h);
        drawFaceBB();
    };
    xhr.send(body);
}

// drawFaceBB();

function postTest() {
    const body = new FormData();
    body.append('test', 'test from JS');
    xhr.open('POST', 'http://localhost:8000/test', true);
    xhr.onload = () => {
        res = JSON.parse(xhr.responseText);
        console.log(res)
        getTest()
    };
    xhr.send(body);
}

function getTest() {
    const body = new FormData();
    xhr.open('GET', 'http://localhost:8000/', true);
    xhr.onload = () => {
        // res = JSON.parse(xhr.responseText);
        console.log(xhr.responseText)
    };
    xhr.send(body);
}

// var uri = 'ws://localhost:60000';

// window.onload = function () {
//     connection = new WebSocket(uri);
//     connection.onopen = onOpen;
//     connection.onmessage = onMessage;
// };

// function onOpen(event) {
//     console.log('Connect successful!');
//     websocketSend(canvas.toDataURL('image/jpeg').replace(/^.*,/, ''));
// }

// function onMessage(event) {
//     //Incoming data
//     res = JSON.parse(event.data.replace(/'/g, '"'));
//     if (res.x !== 0) {
//         context2.clearRect(0, 0, video.width, video.height);
//         context2.strokeRect(res.x, res.y, res.w, res.h);
//     }
//     // setInterval(function () {
//     //     websocketSend(canvas.toDataURL('image/jpeg').replace(/^.*,/, ''));
//     // }, 100);
//     websocketSend(canvas.toDataURL('image/jpeg').replace(/^.*,/, ''));
// }

// function websocketSend(data) {
//     //Send data
//     connection.send(data);
// }
