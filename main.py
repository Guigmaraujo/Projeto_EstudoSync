import  requests
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

  email = request.json['email']
  senha = request.json['senha']

  usuario_existe = False

  with open('cadastro.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    if email in conteudo:
      login_arquivo = open('login.txt', 'a')
      login_arquivo.write(f'{str(email)}' + '\n')
      login_arquivo.write(f'{str(senha)}' + '\n')
      usuario_existe = True

  if usuario_existe:
    return jsonify({'sucesso': True})
  else:
    return jsonify({'sucesso': False})

@app.route('/cadastro', methods=['POST'])
def cadastro():

  cadastro = request.json

  cadastro_arquivo = open('cadastro.txt', 'a')
  cadastro_arquivo.write(f'{str(cadastro)}' + '\n')

  return jsonify(cadastro)


if __name__ == '__main__':
  app.run(host='0.0.0.0')