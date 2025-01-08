from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'

todos={}

@app.route('/')
def index():
    user_todos = todos.get(session['username'],[])
    return render_template('todos.html',
                           username=session['username'],
                           todos=user_todos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index')) #redirect 글로 보내줄께 인덱스에 있는 url로 가줘. index는 바로 위의 함수
    
    return render_template('login.html')

@app.route('/add', methods=['POST']) #add는 추가하는 거 
def add_todo():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    new_todo = request.form['todo'] #유저네임 있으면 
    if new_todo:
        if session['username'] not in todos: #투두와 유저네임이 같지 않으면
            todos[session['username']] = []
        todos[session['username']].append(new_todo) #리스트에 넣어놓는거

    return redirect(url_for('index'))

if __name__== '__main__':
    app.run(debug=True)