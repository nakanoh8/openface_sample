# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, abort, make_response, render_template, url_for, flash, redirect
from jinja2 import Template
import time
import asyncio

import main
import ws_server

import threading

template = Template('Hello {{ name }}!')

api = Flask(__name__)

@api.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
    # Unicodeにしたくない場合は↓
    # return make_response(json.dumps(result, ensure_ascii=False))
@api.route('/face_bb', methods=['POST'])
def face_bb():
    face_bb = main.get_face_bounding_box(request.form["img"])
    return make_response(face_bb)

@api.route('/face_recog', methods=['POST'])
def face_recog():
    res = main.face_recog(request.form["img"])
    return make_response(res)

def new_client(client, server):
    server.send_message_to_all("New client has joined")

def send_msg_allclient(client, server, message):
    server.send_message_to_all(message)

def worker1():
    # thread の名前を取得
    api.run(host='0.0.0.0', port=3000)

def worker2():
    ws_server.run(host='0.0.0.0', port=60000)

if __name__ == '__main__':
    # スレッドに workder1 関数を渡す
    t1 = threading.Thread(target=worker1)
    # t2 = threading.Thread(target=worker2)
    # スレッドスタート
    t1.start()
    # t2.start()
    print('started')