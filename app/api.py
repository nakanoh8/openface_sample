# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, abort, make_response, render_template, url_for, flash, redirect
from jinja2 import Template
import time
import asyncio

from . import service

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/face_bb', methods=['POST'])
def face_bb():
    face_bb = service.get_face_bounding_box(request.form["img"])
    return make_response(face_bb)

@api.route('/face_recognition', methods=['POST'])
def face_recognition():
    res = service.face_recog(request.form["img"])
    return make_response(res)

@api.route('/test', methods=['POST'])
def test():
    res = service.postTest()
    print(res)
    return make_response(res)

# ----------------
# WebSocket使用パターン
# ----------------
# def new_client(client, server):
#     server.send_message_to_all("New client has joined")
# def send_msg_allclient(client, server, message):
#     server.send_message_to_all(message)