import openface_func

import base64
import numpy as np
import cv2
import requests
import chardet
import data_uri

def signup(user_id, capture_img):
    face_vct_1 = openface_func.getFaceVector(capture_img)
    if face_vct_1 is None:
        return None
    user = { "user_id" : user_id, "face_vct_1": face_vct_1}
    ###
    ###

def face_recog(capture_img):
    # 認証時の撮影画像から顔ベクトル(認証ベクトル)を取得
    # OK: 顔ベクトルを返却 / NG: Noneを返却
    capture_img_vec = openface_func.getFaceVector(capture_img)
    if capture_img_vec is None:
        return None
    # OK
    # 認証ベクトル一覧を取得→ループして各データに対してベクトル間の距離を取得
    # 距離が設定した閾値(1.0)以下となるデータが存在した場合、スマートロックを解錠する
    sample_img_vec = openface_func.get_face_vector("/root/openface/images/examples/lennon-2.jpg")
    res = openface_func.get_face_distance(capture_img_vec, sample_img_vec)
    print(res)
    return res
    #####

def get_face_bounding_box(capture_img_base64):
    # encode=base64.b64encode(capture_img_base64)
    # with open("base64.txt","wb") as f:
    #     f.write(capture_img_base64.encode())

    # print("### capture_img_base64", type(capture_img_base64))
    # i = get_sync(capture_img_base64)
    # print("### i", i)
    # encode=base64.b64encode(capture_img_base64)
    # print("### encode", type(encode))
    #バイナリデータ <- base64でエンコードされたデータ  
    capture_img_binary = base64.b64decode(capture_img_base64)
    # print("### capture_img_binary", type(capture_img_binary))
    capture_img_jpg=np.frombuffer(capture_img_binary, dtype=np.uint8)
    # print("### capture_img_jpg", type(capture_img_jpg))
    #raw image <- jpg
    capture_img = cv2.imdecode(capture_img_jpg, cv2.IMREAD_COLOR)
    # print("### capture_img", type(capture_img))
    #デコードされた画像の保存先パス
    image_file="/home/app/capture_img.jpg"
    #画像を保存する場合
    cv2.imwrite(image_file, capture_img)
    bb = openface_func.get_face_bounding_box("/home/app/capture_img.jpg")
    # print(bb)
    return bb


# faceCheck("/root/openface/images/examples/lennon-1.jpg")