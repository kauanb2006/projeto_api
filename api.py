from flask import Blueprint,jsonify,request
bp = Blueprint ("api",__name__)

@bp.route("/")
def index():
 # Função que retorna o JSON com status 200 e a mensagem "API do SEU_NOME_COMPLETO".
  return {"status": 200, "message": "API do {}".format([ "Kauan Barbosa Lopes"])}
@bp.route("/api/aleatorios")
def aleatorios():
  import random
  a = random.randint(49,100)
  return jsonify({"status" : 200 , "data" : a})

@bp.route("/api/argumentos/ < string : nome>")
def argumentos (nome: str):
  return jsonify ({ "status" : 200 ,"data " : nome })


