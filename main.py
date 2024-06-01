from flask import Flask
from flask import render_template
from flask import request
from flask_socketio import SocketIO
from flask_socketio import join_room
from flask_socketio import leave_room
from flask_socketio import send
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('user_joined')
def on_user_joined(data):
    print('user joined' + str(data))

@app.route('/join')
def page_join():
    return render_template('join.html')

@app.route('/room/<room>')
def page_room(room):
    return render_template('room.html', room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)