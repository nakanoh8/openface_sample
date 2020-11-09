import time

start = time.time()

import argparse
import cv2
import itertools
import os

import numpy as np
np.set_printoptions(precision=2)

import openface

fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, '/root/openface', 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')
openfaceModelDir = os.path.join(modelDir, 'openface')

parser = argparse.ArgumentParser()
parser.add_argument('--dlibFacePredictor', type=str, help="Path to dlib's face predictor.",
                    default=os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))
parser.add_argument('--networkModel', type=str, help="Path to Torch network model.",
                    default=os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'))
parser.add_argument('--imgDim', type=int,
                    help="Default image dimension.", default=96)
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()
align = openface.AlignDlib(args.dlibFacePredictor)
net = openface.TorchNeuralNet(args.networkModel, args.imgDim)

# 顔ベクトル取得
def get_face_vector(bgrImg):
    # bgrImg = cv2.imread(imgPath)
    # if bgrImg is None:
    #     raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        return None
    alignedFace = align.align(args.imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    # if alignedFace is None:
    #     raise Exception("Unable to align image: {}".format(imgPath))
    rep = net.forward(alignedFace)
    return to_arr(rep)

# 顔ベクトル間の距離を取得
def get_face_distance(imgVec1, imgVec2):
    d = to_ndarr(imgVec1) - to_ndarr(imgVec2)
    return float("{:0.3f}".format(np.dot(d, d)))

def to_arr(ndarr):
    return ndarr.tolist()

def to_ndarr(arr):
    return np.array(arr)

# 顔の抽出範囲座標の4点を取得
def get_face_bounding_box(bgrImg):
    # bgrImg = cv2.imread(imgPath)
    # print("bgrImg", type(bgrImg))
    if bgrImg is None:
        return {"x": 0, "y": 0, "w": 0, "h": 0}
        # raise Exception("Unable to load image: {}".format(imgPath))

    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    # print("rgbImg", type(rgbImg))
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        print("#### No face")
        return {"x": 0, "y": 0, "w": 0, "h": 0}
    return {
        "x": bb.left(), 
        "y": bb.top(), 
        "w": bb.right() - bb.left(), 
        "h": bb.bottom() - bb.top()
        }
