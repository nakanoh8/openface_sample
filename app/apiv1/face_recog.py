from flask import Blueprint, make_response, request

from . import api
from .. import service

@api.route('/face_recognition', methods=['POST'])
def face_recognition():
    res = service.face_recog(request.form["img"])
    return make_response(res)