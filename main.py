# FrontEnd -> parte visual
    # html, javascript, css
# Backend -> a logica de funcionamento nos bastidores
    # python, java, c
# Framework -> Flask -> criar site
# ambiente virtual -> local no seu computador c instalações específicas

# Import o flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Cria um aplicativo por meio do flask
app = Flask(__name__)

# permite que mensagens sejam enviadas de qualquer usuario
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# Criar a primeira página = 1° rota "/"; rota - variações que existe dentro de um site
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Roda o aplicativo
socketio.run(app, host="192.168.15.6")

# websocket -> tunel