from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
socketio = SocketIO(app)

messages=[]

@app.route('/loginsuccess')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    username= session['username']
    return render_template('loginsuccess.html',messages=messages, username=username)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index')) #redirect 글로 보내줄께 인덱스에 있는 url로 가줘. index는 바로 위의 함수
    return render_template('login.html')

@socketio.on('message') #소켓에 메시지를 보냄
def handle_message(data):#함수를 관리해줘
    message = {
        'user': session['username'],
        'message': data['message']
    }#유저와 메시지를 나눠 저장장
    messages.append(message)#메시지에 메시지를 넣어줌. 유저이름과 내용을
    emit('message', message, broadcast=True)#메시지를 보고 있는 모든 사람들에게 알려줌줌

if __name__== '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)