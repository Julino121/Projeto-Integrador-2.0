import json
from flask import Flask, request, render_template
import socket

app = Flask(__name__)

def enviar_dados_para_servidor_java(dados_validar):
    host = "localhost"
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    # Convert the data to the format expected by the Java server
    dados_formatados = ":".join([f"{key}:{value}" for key, value in dados_validar.items()])

    # Send a message to the Java server
    sock.sendall(dados_formatados.encode())

    # Disable writing to the client socket
    sock.shutdown(socket.SHUT_WR)
    print(f"Dados enviados para validação: {dados_validar}")

    # Receive a response from the Java server
    response = sock.recv(1024).decode()
    
    # Check if a valid response is received
    if response is not None:
        response = "Recebido do servidor Java: " + response
    else:
        response = "Nenhuma resposta válida recebida do servidor Java."
    return response

@app.route('/')
def index():
    return render_template('form.html')

@app.route("/style_form", methods=['POST'])
def formulario():
    global dados_validar
    

    dados_validar = {
        "name": request.form["name"],
        "cpf": request.form["cpf"],
        "email": request.form["email"]
    }
    
    resposta = enviar_dados_para_servidor_java(dados_validar)
    print(resposta)

    if resposta == "VALIDADO":
        dados_formulario = {
                "name": request.form["name"],
                "cpf": request.form["cpf"],
                "phone": request.form["phone"],
                "email": request.form["email"],
                "country": request.form["country"],
                "state": request.form["state"],
                "cep": request.form["cep"],
                "street": request.form["street"],
                "neighborhood": request.form["neighborhood"],
                "complement": request.form["complement"],
                "specialty": request.form["specialty"],
                "clinic": request.form["clinic"],
                "insurance": request.form["insurance"],
                "date": request.form["date"],
                "time": request.form["time"]
            }
    else:
        print("DADOS INVÁLIDOS, tente novamente...")

if __name__ == '__main__':
    app.run(host='localhost', port=80)