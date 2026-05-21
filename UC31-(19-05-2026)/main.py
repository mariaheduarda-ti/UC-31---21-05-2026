from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('prática.html')

@app.route('/autenticar', methods = ['GET'])
def autenticar():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    return "Nome {} e Curso {}".format(nome, curso)

if __name__=='__main__':
    app.run(debug=True)