from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
 # Função que retorna o JSON com status 200 e a mensagem "API do SEU_NOME_COMPLETO".
  return {"status": 200, "message": "API do {}".format([ "Kauan Barbosa Lopes"])}
@app.route("/aleatorios")
def aleatorios():
  import random
  a = random.randint(49,100)
  return jsonify({"status" : 200 , "data" : a})

@app.route("/argumentos/ < string : nome>")
def argumentos (nome: str):
  return jsonify ({ "status" : 200 ,"data " : nome })

if __name__ == "__main__":
  app.run(debug=True)

