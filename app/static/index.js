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
    context.drawImage(video, 0, 0, video.width, video.height);
    // var a = document.createElement('a');
    // //canvasをJPEG変換し、そのBase64文字列をhrefへセット
    // a.href = canvas.toDataURL('image/jpeg'); //base64でデータ化
    // //ダウンロード時のファイル名を指定
    // img_file_name = Math.random().toString(32).substring(2);
    // a.download = img_file_name + '.jpg';
    // //クリックイベントを発生させる
    // a.click();
    postFaceRecog(canvas.toDataURL('image/jpeg'));
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
        authenticate();
    }
});

function drawFaceBB() {
    console.log('run drawFaceBB()');
    postFaceBB(canvas.toDataURL('image/jpeg').replace(/^.*,/, ''));
}

function postFaceRecog() {
    xhr.open('POST', 'http://localhost:3000/face_recog', true);
    xhr.setRequestHeader(
        'content-type',
        'application/x-www-form-urlencoded;charset=UTF-8'
    );
    // フォームに入力した値をリクエストとして設定
    var request = 'filename=' + img_file_name;
    // サーバからのデータ受信を行った際の動作
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
            }
        }
    };
    xhr.send(request);
}

function postFaceBB(cap_img) {
    const body = new FormData();
    body.append('img', cap_img);
    xhr.open('POST', 'http://localhost:3000/face_bb', true);
    xhr.onload = () => {
        console.log(xhr.responseText);
        res = JSON.parse(xhr.responseText);
        context2.clearRect(0, 0, video.width, video.height);
        context2.strokeRect(res.x, res.y, res.w, res.h);
        drawFaceBB();
    };
    xhr.send(body);
}
drawFaceBB();
// setInterval(drawFaceBB, 300);
