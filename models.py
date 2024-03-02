from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    rua = db.Column(db.String(120), nullable=False)
    bairro = db.Column(db.String(120), nullable=False)
    cidade = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(120), nullable=False)
    cep = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(120), nullable=False)
    identidade = db.Column(db.String(120), nullable=False)
    habilitacao = db.Column(db.String(120), nullable=False)
    vencimento = db.Column(db.String(120), nullable=False)


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(120), nullable=False)
    modelo = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.String(120), nullable=False)
    placa = db.Column(db.String(120), nullable=False)
    chassi = db.Column(db.String(120), nullable=False)
    cor = db.Column(db.String(120), nullable=False)
    combustivel = db.Column(db.String(120), nullable=False)
