//動画流す準備
var video = document.getElementById('video');
// getUserMedia によるカメラ映像の取得
var media = navigator.mediaDevices.getUserMedia({ video: true });
//リアルタイムに再生（ストリーミング）させるためにビデオタグに流し込む
media.then((stream) => {
    video.srcObject = stream;
});

var img_file_name = null;

function saveCaptureImg() {
    console.log('up');
    var canvas = document.getElementById('canvas');

    canvas.setAttribute('width', video.width);
    canvas.setAttribute('height', video.height);
    context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, video.width, video.height);
    // context.strokeStyle = '#FF0000';
    // context.strokeRect(400, 300, 100, 150);

    // var a = document.createElement('a');
    // //canvasをJPEG変換し、そのBase64文字列をhrefへセット
    // a.href = canvas.toDataURL('image/jpeg'); //base64でデータ化
    // //ダウンロード時のファイル名を指定
    // img_file_name = Math.random().toString(32).substring(2);
    // a.download = img_file_name + '.jpg';
    // //クリックイベントを発生させる
    // a.click();
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
        console.log('pushed capture');
        saveCaptureImg();
        post();
    }
});

xhr = new XMLHttpRequest();

// サーバからのデータ受信を行った際の動作
xhr.onload = function (e) {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
        }
    }
};

function post() {
    xhr.open('POST', 'http://localhost:3000/imgcheck', true);
    xhr.setRequestHeader(
        'content-type',
        'application/x-www-form-urlencoded;charset=UTF-8'
    );
    // フォームに入力した値をリクエストとして設定
    var request = 'filename=' + img_file_name;
    xhr.send(request);
}
