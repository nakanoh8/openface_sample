# openface_sample
  
## 顔認証サンプルコードの動作確認手順
  
### Dockerのインストール
{参考記事}
  
### ローカルの作業ディレクトリへGitプロジェクトをclone
cd {作業ディレクトリ}  
git clone ・・・・
※clone済みの場合は、最新化する
  
### 顔認証Dockerfileをbuildしてイメージを作成
cd {作業ディレクトリ}/ict_store/exxxxxx/face_recognition
docker build -t ict_store/face_recognition:1.0 .
※完了まで少し時間がかかるので待機
  
### イメージをrunしてコンテナを作成 （ローカルの作業ディレクトリとコンテナのhomeディレクトリを共有）
docker run -it -v {作業ディレクトリの絶対パス(pwd)}/ict_store/exxxxxx/:/home/ ict_store/face_recognition:1.0 /bin/bash
  
### コンテナ上で顔認証サンプルコードを実行
python3 /home/face_recognition/main.py  
  
#### 実行結果  
・・・・・・・・・・  
  
#### 顔認証ソースファイル構成
・main.py　・・・　顔認証実行ファイル（動作確認用サンプル）。OpenFaceを用いた関数群（openface_func.py）を利用。  
・openface_func.py ・・・　OpenFaceを用いた関数群。「顔ベクトル取得」「顔ベクトル間の距離取得」関数を持つ。
  
## 参考記事
  
### Dockerコマンド よく使うやつ
https://qiita.com/Esfahan/items/52141a2ad741933d7d4c
  
### OpenFace動作環境作成
https://elsammit-beginnerblg.hatenablog.com/entry/2020/05/17/192559
https://blog.goo.ne.jp/jsp_job/e/a779b628252e23a4ebcf6c857e748f2f

