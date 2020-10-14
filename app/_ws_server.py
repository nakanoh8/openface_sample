from websocket_server import WebsocketServer

import service

def new_client(client, server):
    server.send_message_to_all("New client has joined")

def send_msg_allclient(client, server, message):
    face_bb = service.get_face_bounding_box(message)
    server.send_message_to_all(str(face_bb))

def run(host, port):
    print("ws run")
    server = WebsocketServer(port, host)
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(send_msg_allclient)
    server.run_forever()