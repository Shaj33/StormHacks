from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app=app, cors_allowed_origins="*")

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on("videoChange")
def handle_videochange(json, methods=['GET', 'POST']):
    print('received call to adjust video time: ' + str(json))
    socketio.emit('changeVideo', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
