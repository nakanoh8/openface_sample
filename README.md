# openface_sample

## 手順

### ローカルの作業ディレクトリへGitClone
cd {作業ディレクトリ}  
git clone ict_store_face_check  
cd ict_store_face_check

### Dockerfileをbuildしてイメージを作成
docker build -t ict_store_face_check:1.0 .

### イメージをrunしてコンテナを作成（ローカルの作業ディレクトリとコンテナのhomeディレクトリを共有）
docker run -it -v {作業ディレクトリの絶対パス(pwd)}:/home/ ict_store_face_check:1.0 /bin/bash

### コンテナでサンプルコード実行
python3 /home/ict_store_face_check/main.py

## Dockerfile作成時の参考記事
https://elsammit-beginnerblg.hatenablog.com/entry/2020/05/17/192559
https://blog.goo.ne.jp/jsp_job/e/a779b628252e23a4ebcf6c857e748f2f

