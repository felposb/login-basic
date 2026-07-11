from flask import Flask, jsonify, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
DADOS = 'dados/dados.json'
def carregar(a):
    with open(a, 'r') as f:
        return json.load(f)
    
def salvar(a, d):
    with open(a, 'w') as f:
        json.dump(d, f, indent=4)

def validacao():
    dados = request.json
    campos = [
        ("email", str, True),
        ("senha", str, True),
    ]
    for campo, tipo, obrigatorio in campos:
        valor = dados.get(campo)
        if obrigatorio and(campo not in dados or valor == ''):
            return jsonify({"erro": f"{campo} é obrigatorio"}),400
        if campo in dados and not isinstance(valor, tipo):
            return jsonify({"erro": f"{campo} apenas recebe {tipo.__name__}"}), 422
def proximo_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1
@app.post("/dados")
def criar():
    dado = carregar(DADOS)
    dados = request.json
    validar = validacao()
    if validar:
        return validar    
    
    novo_dado = {
        "id": proximo_id(dado),
        "email": dados.get("email"),
        "senha": dados.get("senha")
    }
    dado.append(novo_dado)
    salvar(DADOS, dado)
    return jsonify({"mensagem": "Criado com sucesso"}), 201

app.run(debug=True)