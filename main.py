from flask import Flask,request
from flask_socketio import SocketIO, send, emit, join_room, leave_room

rooms = {}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handle_message(message):
    print("Session ID:"+request.sid);
    print(message);
    for room in rooms:
        if request.sid in rooms[room]:
            for user in rooms[room]:
                print(room);
                if user != request.sid:
                    send(message, room=user);
                    print(request.sid+" sent message: "+message['message']+" to "+user);


@socketio.on('join')
def handle_join(data):
    room = [request.sid, data['roomId']];
    rooms['room_'+data['roomId']]=room;
    print(request.sid+" joins "+data['roomId']);
    print(rooms);

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000);
