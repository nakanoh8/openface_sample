from flask import Blueprint, make_response, request

from . import api
from .. import service

@api.route('/face_bb', methods=['POST'])
def face_bb():
    face_bb = service.get_face_bounding_box(request.form["img"])
    return make_response(face_bb)