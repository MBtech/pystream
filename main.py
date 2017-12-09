# main.py

from flask import Flask, render_template, Response
from camera import VideoCamera
from requires_authorization import requires_authorization
from app import app
from gevent.wsgi import WSGIServer
import ssl
import yaml
from server import get_frame

@app.route('/')
@requires_authorization
def index():
    return render_template('index.html')

def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
@requires_authorization
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    with open("credentials.yaml", 'r') as stream:
        data_loaded = yaml.load(stream)
    app.config['USERNAME'] = data_loaded['username']
    app.config['PASSWORD'] = data_loaded['password']
    httpd = WSGIServer(('127.0.0.1', 5000), app, certfile='./server.cert', keyfile='./server.pem')
    httpd.serve_forever()
