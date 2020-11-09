from flask import Flask
from flask_cors import CORS, cross_origin
from .apiv1 import api

app = Flask(__name__)
CORS(app, support_credentials=True)
# 分割したblueprintを登録する
app.register_blueprint(api)