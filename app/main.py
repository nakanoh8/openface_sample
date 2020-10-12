import openface_func

import base64
import numpy as np
import cv2
import requests
import chardet
import json

auth_ok_thr = 0.3

def signup(user_id, capture_img):
    face_vct_1 = openface_func.getFaceVector(capture_img)
    if face_vct_1 is None:
        return None
    user = { "user_id" : user_id, "face_vct_1": face_vct_1}
    ###
    ###

def face_recog(img_base64):
    img_binary = base64.b64decode(img_base64)
    img_jpg=np.frombuffer(img_binary, dtype=np.uint8)
    #raw image <- jpg
    img = cv2.imdecode(img_jpg, cv2.IMREAD_COLOR)
    # #デコードされた画像の保存先パス
    # image_file="/home/app/static/img/auth_img.jpg"
    # if img is None:
    #     return "CAPTURE_IMG_ERROR"
    # #画像を保存する場合
    # cv2.imwrite(image_file, img)

    # 認証時の撮影画像から顔ベクトル(認証ベクトル)を取得
    # OK: 顔ベクトルを返却 / NG: Noneを返却
    img_vec = openface_func.get_face_vector(img)
    if img_vec is None:
        return "NO_CONTAINS_FACE"
    # OK
    json_open = open('/home/app/static/users.json', 'r')
    json_load = json.load(json_open)
    for user in json_load:
        d = openface_func.get_face_distance(img_vec, user["face_vector"])
        if d <= auth_ok_thr:
            return "AUTH_OK: [GET_DISTANCE] " + str(d)
        return "AUTH_NG: [GET_DISTANCE] " + str(d)

    return "AUTH_NG"
    #####

# print(openface_func.get_face_vector("/home/app/static/img/hayato-1.jpg"))

def get_face_bounding_box(img_base64):
    #バイナリデータ <- base64でエンコードされたデータ  
    img_binary = base64.b64decode(img_base64)
    img_jpg=np.frombuffer(img_binary, dtype=np.uint8)
    #raw image <- jpg
    img = cv2.imdecode(img_jpg, cv2.IMREAD_COLOR)
    # print("cv2.imdecode", type(img))
    # #デコードされた画像の保存先パス
    # image_file="/home/app/static/img/capture_img.jpg"
    # if img is None:
    #     return {"x": 0, "y": 0, "w": 0, "h": 0}
    # #画像を保存する場合
    # cv2.imwrite(image_file, img)
    bb = openface_func.get_face_bounding_box(img)
    return bb