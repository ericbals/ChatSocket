import socketio
from aiohttp import web
# create a Socket.IO server
sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

users = []
messageHistory = []

#find a user in the DB by sid
def searchUserBySid(sid):
    for user in users:
        if user['sid'] == sid:
            return user
    return None

# default connection
@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    begin_chat(sid)
    await sio.emit('mysid', {'data': sid, 'users': users}, room=sid)

#default disconnection
@sio.event
def disconnect(sid):
    exit_chat(sid)
    print('disconnect ', sid)

#add a new user to DB
@sio.on('newUser')
def addUser(sid, data):
    if data not in users: 
        users.append(data)

#send to client all the messages
@sio.on('getAllMessages')
async def getAllMessages(sid):
    await sio.emit('messageHistory', {'data': messageHistory}, room=sid)

#receive a message and add it to the db
@sio.on('message')
def addMessageToHistory(sid, data):
    messageHistory.append({'sid': sid, 'user': searchUserBySid(sid), 'message': data})

@sio.event
def begin_chat(sid):
    sio.enter_room(sid, 'chat_users')

@sio.event
def exit_chat(sid):
    sio.leave_room(sid, 'chat_users')

@sio.event
def my_message(sid, data):
    sio.emit('my reply', data, room='chat_users', skip_sid=sid)

@sio.on('*')
def catch_all(event, sid, data):
    pass

if __name__ == '__main__':
    web.run_app(app)