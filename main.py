from flask import Flask, redirect, render_template, request, url_for
from model import myModel

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['pic']
    if uploaded_file.filename != '':
        uploaded_file.save('pics/' + uploaded_file.filename)
        myModel(uploaded_file.filename)
    return redirect(url_for('hello/'))