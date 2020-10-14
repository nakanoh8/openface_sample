from flask import Blueprint, render_template

from . import api

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')