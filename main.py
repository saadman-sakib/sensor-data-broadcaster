from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@socketio.on('data_send')
def data_receive(data):
    # print('received data: ' + str(data))
    emit('data_send', data, broadcast=True)


@socketio.on('connect')
def data_receive(data):
    print('connected')
    print(data)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    socketio.run(app)