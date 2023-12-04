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
        response = response
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
    if resposta.strip().lower() == "validado":
        print("VALIDADOS")
        name, cpf, phone, email, country, state, cep, street, neighborhood, complement, specialty, clinic, insurance, date, time = extract_data(dados_formulario)
        insert_usuario(name, cpf, email, phone, cep, street)
        insert_consulta(name, clinic, specialty, insurance, date, time)
        insert_pacient(name)
        return 0
    else:
        print("INVALIDO, preencha o formulario novamente")
        return 0
    
def extract_data(dados_formulario):
    name = dados_formulario["name"]
    cpf = dados_formulario["cpf"]
    phone = dados_formulario["phone"]
    email = dados_formulario["email"]
    country = dados_formulario["country"]
    state = dados_formulario["state"]
    cep = dados_formulario["cep"]
    street = dados_formulario["street"]
    neighborhood = dados_formulario["neighborhood"]
    complement = dados_formulario["complement"]
    specialty = dados_formulario["specialty"]
    clinic = dados_formulario["clinic"]
    insurance = dados_formulario["insurance"]
    date = dados_formulario["date"] 
    time = dados_formulario["time"]



    return name, cpf, phone, email, country, state, cep, street, neighborhood, complement, specialty, clinic, insurance, date, time




def insert_usuario(name, cpf, phone, email, cep, street):
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Eli210504.",
        database="pi4DataBase"
    )

    mycursor = mydb.cursor()

    # SQL query with placeholders for parameters
    sql = "INSERT INTO usuarios (name, cpf, phone, email, cep, rua) VALUES (%s,%s,%s,%s,%s)"

    # Tuple with values obtained from the form or any other source
    val = (name, cpf, phone, email, cep, street)
    # Execute the query with the provided values
    mycursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()


def insert_consulta(name, clinic, specialty, insurance, date, time):
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Eli210504.",
        database="pi4DataBase"
    )
    mycursor = mydb.cursor()

    select_query = "SELECT id_usuario FROM usuario WHERE name = %s"
    mycursor.execute(select_query, (name))
    id_usuario = mycursor.fetchone()

    select_query = "SELECT id_clinica FROM clinica WHERE name = %s"
    mycursor.execute(select_query, (clinic))
    id_clinica = mycursor.fetchone()



    sql = "INSERT INTO consulta (id_usuario, id_clinica, specialty, insurance, date, time VALUES (%s,%s,%s,%s,%s,%s)"

    val= (id_usuario, id_clinica, specialty, clinic, insurance, date, time)

    mycursor.execute(sql, val)
    mydb.commit()




def insert_pacient(name):
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Eli210504.",
        database="pi4DataBase"
    )

    mycursor = mydb.cursor()
    
    select_query = "SELECT id_usuario FROM usuario WHERE usuario = %s"
    mycursor.execute(select_query, (name))
    id_usuario = mycursor.fetchone()

    select_query = "SELECT id_consulta FROM consulta WHERE id_usuario = %s"
    mycursor.execute(select_query, (id_usuario))
    id_consulta = mycursor.fetchone()

    sql = "INSERT INTO patiet (id_clinica, id_usuario) VALUES (%s,%s)"

    # Tuple with values obtained from the form or any other source
    val = (id_usuario , id_consulta)
    # Execute the query with the provided values
    mycursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()




if __name__ == '__main__':
    app.run(host='localhost', port=80)

if __name__ == '__main__':
    app.run(host='localhost', port=80)
