from flask import Blueprint, make_response, request
import json

from . import api
from .. import service

@api.route('/face_bb', methods=['POST'])
def face_bb():
    data = json.loads(request.data.decode('utf-8'))
    face_bb = service.get_face_bounding_box(data["img"])
    return make_response(face_bb)