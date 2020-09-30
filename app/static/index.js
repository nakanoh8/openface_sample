//動画流す準備
var video = document.getElementById('video');
// getUserMedia によるカメラ映像の取得
var media = navigator.mediaDevices.getUserMedia({ video: true });
//リアルタイムに再生（ストリーミング）させるためにビデオタグに流し込む
media.then((stream) => {
    video.srcObject = stream;
});

function saveCaptureImg() {
    var canvas = document.getElementById('canvas');

    canvas.setAttribute('width', video.width);
    canvas.setAttribute('height', video.height);
    canvas.getContext('2d').drawImage(video, 0, 0, video.width, video.height);

    var a = document.createElement('a');
    //canvasをJPEG変換し、そのBase64文字列をhrefへセット
    a.href = canvas.toDataURL('image/jpeg'); //base64でデータ化
    //ダウンロード時のファイル名を指定
    a.download = 'download.jpg';
    //クリックイベントを発生させる
    a.click();
}

document.addEventListener('keydown', (event) => {
    var keyName = event.key;
    if (keyName === ' ') {
        console.log(`keydown: SpaceKey`);
        console.log('pushed capture');
        saveCaptureImg();
    }
});
