import openface_func


def faceCheck(input_img):
    # 認証時の撮影画像から顔ベクトル(認証ベクトル)を取得
    # OK: 顔ベクトルを返却
    # NG: Noneを返却
    input_img_vec = openface_func.getFaceVector(input_img)

    if input_img_vec is None:
        return None

    # NGの場合
    # 顔ベクトル取得失敗ログ出力
 
    # OKの場合
    # 認証ベクトル一覧を取得→ループして各データに対してベクトル間の距離を取得
    # 距離が設定した閾値(1.0)以下となるデータが存在した場合、スマートロックを解錠する

    # 顔照合失敗ログ出力
    

    ##### 顔比較サンプル
    sample_img_vec = openface_func.getFaceVector("/root/openface/images/examples/lennon-2.jpg")
    res = openface_func.getDistance(input_img_vec, sample_img_vec)
    print(res)
    return res
    #####

def getFaceBoundingBox(input_img):
    return openface_func.getFaceBoundingBox(input_img)


# faceCheck("/root/openface/images/examples/lennon-1.jpg")