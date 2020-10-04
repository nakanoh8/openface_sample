# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, abort, make_response, render_template, url_for, flash, redirect
from jinja2 import Template
import time

import main

template = Template('Hello {{ name }}!')

api = Flask(__name__)

@api.route('/test', methods=['GET'])
def get_test():
    return render_template('index.html')
    # Unicodeにしたくない場合は↓
    # return make_response(json.dumps(result, ensure_ascii=False))

@api.route('/imgcheck', methods=['POST'])
def imgcheck():
    time.sleep(1)
    res = main.faceCheck("/home/downloads/" + request.form["filename"] + ".jpg")
    if res is None:
        return make_response("Face is none")
    return make_response(
        main.faceCheck("/home/downloads/" + request.form["filename"] + ".jpg")
        )

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)