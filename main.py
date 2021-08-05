from flask import session
from Website import app, create_database, db
from flask_socketio import SocketIO
from Website.database import Messages


app = app
socketio = SocketIO(app)

@socketio.on('event')
def handle_message(msg):
    if 'name' in msg:
        message = Messages(message=msg['message'], user_name=msg['name'])
        db.session.add(message)
        db.session.commit()
    else:
        if 'name' in session:
            msg['name'] = session['name']
            print(msg)
    socketio.emit('response', msg)

if __name__ == "__main__":
    create_database(app, db)
    socketio.run(app)
