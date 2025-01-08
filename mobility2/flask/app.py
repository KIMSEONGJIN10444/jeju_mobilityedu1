from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello() :
    return render_template('index.html')

@app.route('/app')
def apps() :
    return "안녕하세요! app입니다!"

@app.route('/<name>')
def callme(name):
    return render_template('name.html', user = name)

if __name__ == '__main__':
    app.run(debug = True)