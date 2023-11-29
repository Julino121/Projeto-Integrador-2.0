from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personal_info = db.Column(db.JSON)
    address = db.Column(db.JSON)
    appointment = db.Column(db.JSON)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    form_data = FormData(
        personal_info=data['personalInfo'],
        address=data['address'],
        appointment=data['appointment']
    )

    db.session.add(form_data)
    db.session.commit()

    return jsonify({'message': 'Dados recebidos e salvos com sucesso!'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
