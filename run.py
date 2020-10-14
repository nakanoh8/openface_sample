from flask import Flask
from app.server import app
from app.apiv1 import api

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

# ----------------
# WebSocket使用パターン
# ----------------
# import ws_server
# import threading
# def worker1():
#     api.run(host='0.0.0.0', port=3000)
# def worker2():
#     ws_server.run(host='0.0.0.0', port=60000)
# if __name__ == '__main__':
    # スレッドに workder1 関数を渡す
    # t1 = threading.Thread(target=worker1)
    # t2 = threading.Thread(target=worker2)
    # スレッドスタート
    # t1.start()
    # t2.start()
    # print('started')