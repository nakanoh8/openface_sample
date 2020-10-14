from flask import Flask
from .apiv1 import api

app = Flask(__name__)
# 分割したblueprintを登録する
app.register_blueprint(api)