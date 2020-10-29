from flask import Blueprint, render_template

from . import api
from .. import service

@api.route('/', methods=['GET'])
def index():
    print("#########")
    # res = service.postTest()
    # print(res)
    return render_template('index.html')