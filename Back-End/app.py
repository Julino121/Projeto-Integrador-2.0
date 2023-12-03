from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Eli210504.@localhost/pi4DataBase'
db = SQLAlchemy(app)

class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cpf = db.Column(db.String(11))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    country = db.Column(db.String(255))
    state = db.Column(db.String(255))
    cep = db.Column(db.String(10))
    street = db.Column(db.String(255))
    neighborhood = db.Column(db.String(255))
    complement = db.Column(db.String(255))
    specialty = db.Column(db.String(255))
    clinic = db.Column(db.String(255))
    insurance = db.Column(db.String(255))
    date = db.Column(db.String(10))
    time = db.Column(db.String(8))

@app.route('/api/receber_dados', methods=['POST'])
def receber_dados():
    data = request.json
    novo_formulario = Formulario(
        name=data['name'],
        cpf=data['cpf'],
        phone=data['phone'],
        email=data['email'],
        country=data['country'],
        state=data['state'],
        cep=data['cep'],
        street=data['street'],
        neighborhood=data['neighborhood'],
        complement=data['complement'],
        specialty=data['specialty'],
        clinic=data['clinic'],
        insurance=data['insurance'],
        date=data['date'],
        time=data['time']
    )
    
    db.session.add(novo_formulario)
    db.session.commit()
    print(novo_formulario)

    return jsonify({'message': 'Dados recebidos com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
