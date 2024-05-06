Documentação da API Flask
Esta documentação descreve uma API web simples criada com o framework Flask. A API oferece três rotas (endpoints) que lidam com diferentes solicitações e retornam respostas no formato JSON.

Funcionalidade
Rota Raiz (/)

Retorna um objeto JSON com o código de status 200 (OK) e uma mensagem contendo seu nome completo.
Rota de Números Aleatórios (/aleatorios)

Gera um número inteiro aleatório entre 49 e 100 (inclusive).
Retorna um objeto JSON com o código de status 200 (OK) e um campo chamado "data" contendo o número aleatório gerado.
Rota de Argumentos (/argumentos/<string:nome>)

Aceita um argumento de rota chamado <nome> que pode conter qualquer valor textual.
Retorna um objeto JSON com o código de status 200 (OK) e um campo chamado "data" contendo o valor do argumento capturado.
Análise do Código
Python
from flask import Flask, jsonify

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define a rota raiz
@app.route("/")
def index():
    # Constrói a resposta JSON com código de status e mensagem
    resposta = {"status": 200, "message": "API do Seu Nome Completo"}
    return jsonify(resposta)  # Converte o dicionário para formato JSON

# Define a rota para gerar um número aleatório
@app.route("/aleatorios")
def aleatorios():
    import random
    # Gera um número aleatório entre 49 e 100
    numero_aleatorio = random.randint(49, 100)
    # Constrói a resposta JSON
    resposta = {"status": 200, "data": numero_aleatorio}
    return jsonify(resposta)  # Converte o dicionário para formato JSON

# Define a rota para manipular argumentos
@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    # Constrói a resposta JSON com o nome fornecido
    resposta = {"status": 200, "data": nome}
    return jsonify(resposta)  # Converte o dicionário para formato JSON

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Executa a aplicação Flask em modo debug
    app.run(debug=True)
Use o código com cuidado.
content_copy
Explicação
Importações:

Flask: Usado para criar a estrutura da aplicação web.
jsonify: Usado para converter dicionários Python em formato JSON para as respostas.
Instância da Aplicação Flask:

app = Flask(__name__): Cria uma instância da aplicação Flask chamada app. O argumento __name__ garante que a aplicação seja identificada corretamente.
Rotas:

Cada rota é definida usando o decorador @app.route, especificando o caminho da URL e a função para lidar com a solicitação.
Rota Raiz (/)
def index(): Esta função é chamada quando a URL raiz (/) é acessada.
A função constrói um dicionário com um código de status de 200 e uma mensagem personalizada contendo seu nome completo.
jsonify(resposta): Converte o dicionário construído (resposta) em formato JSON e o retorna como a resposta para o cliente.
Rota de Números Aleatórios (/aleatorios)
def aleatorios(): Esta função lida com solicitações para o endpoint /aleatorios.
Importa o módulo random e gera um número inteiro aleatório entre 49 e 100 usando random.randint(49, 100).
Uma resposta JSON é criada com o código de status e o número aleatório gerado.
A resposta é convertida para JSON e retornada.
Rota de Argumentos (/argumentos/<string:nome>)
def argumentos(nome: str): Esta função é chamada quando uma solicitação é feita para o caminho /argumentos/<nome>, onde <nome> é um parâmetro dinâmico que pode capturar qualquer valor textual.
O parâmetro é anotado por tipo como str para garantir



tune

share


more_vert
