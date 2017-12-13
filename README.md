# Pystream
A project to setup a private video stream with C.H.I.P and USB camera.
The stream is displayed on a HTTPS webpage that is password protected.

Note: Documentation in progress

## Setup
- Install dependencies using setup.sh script
- Add username and password to credentials.yaml. This is the password that the user will need to access the stream
- Generate self signed certificate with server.pem and server.cert for private key and certificate
`openssl req -x509 -newkey rsa:4096 -keyout server.pem -out server.cert -days 365 -nodes`

## Usage
By default the streaming server is setup on the localhost. This will change soon. 
Start the client side that records the frames using the camera using:
`python client.py`

The run the streaming server using:
`python main.py`

Now you can access the video stream on `https://localhost:5000` using the password and username mentioned in credentials.yaml

### References
https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
https://larsbergqvist.wordpress.com/2016/09/03/basic-authentication-with-python-flask/
http://flask.pocoo.org/snippets/8/
https://github.com/gevent/gevent/blob/master/examples/wsgiserver_ssl.py
http://www.chioka.in/python-live-video-streaming-example/
