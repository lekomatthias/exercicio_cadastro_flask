from app import app
from flask import render_template
from flask import request
from app import cadastro_lib as valid

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/validacao', methods=['GET'])
def validacao():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    cpf = request.args.get('cpf')
    email = request.args.get('email')
    telefone = request.args.get('telefone')


    return "{} {} {} {}".format(valid.Nome_validacao(nome, sobrenome), valid.Cpf_validacao(cpf), 
                             valid.Email_validacao(email), valid.Telefone_validacao('61', telefone))
