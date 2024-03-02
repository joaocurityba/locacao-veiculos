from flask import Flask, render_template, url_for, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)


#Rotas:
@app.route('/')
def index():
    return render_template('base.html')


#Create and Read:
@app.route('/cadastrar_carro', methods=['GET', 'POST'])
def cadastrar_carro():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        placa = request.form['placa']
        chassi = request.form['chassi']
        cor = request.form['cor']
        combustivel = request.form['combustivel']
        new_car = Carro(marca=marca, modelo=modelo, ano=ano, placa=placa, 
                        chassi=chassi, cor=cor, combustivel=combustivel)
        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for('cadastrar_carro'))
    all_users = Carro.query.all()
    return render_template('cadastrar_carro.html', carros=all_users)


#Delete:
@app.route('/delete_carro/<int:carro_id>', methods=['GET', 'POST'])
def delete_carro(carro_id):
    carro = Carro.query.get(carro_id)
    if carro:
        db.session.delete(carro)
        db.session.commit()
        return redirect(url_for('cadastrar_carro'))
    return render_template('cadastrar_carro.html')


#Update:
@app.route('/editar_carro/<int:carro_id>', methods=['GET', 'POST'])
def editar_carro(carro_id):
    carro = Carro.query.get(carro_id)
    if request.method == 'POST':
        carro.marca = request.form['marca']
        carro.modelo = request.form['modelo']
        carro.ano = request.form['ano']
        carro.placa = request.form['placa']
        carro.chassi = request.form['chassi']
        carro.cor = request.form['cor']
        carro.combustivel = request.form['combustivel']
        db.session.commit()
        return redirect(url_for('cadastrar_carro'))
    return render_template('editar_carro.html', carro=carro)


#Rota para criar e ler os clientes:
@app.route('/cadastrar_cliente',  methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        rua = request.form['rua']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        cep = request.form['cep']
        cpf = request.form['cpf']
        rg = request.form['rg']
        habilitacao = request.form['habilitacao']
        vencimento = request.form['vencimento']
        new_cliente = Cliente(nome=nome, rua=rua, bairro=bairro, cidade=cidade, telefone=telefone, cep=cep, cpf=cpf, rg=rg, habilitacao=habilitacao, vencimento=vencimento)
        db.session.add(new_cliente)
        db.session.commit()
        return redirect(url_for('cadastrar_cliente'))
    clientes = Cliente.query.all()
    return render_template('cadastrar_cliente.html', clientes=clientes)


#Rota para editar cliente:
@app.route('/editar_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.rua = request.form['rua']
        cliente.bairro = request.form['bairro']
        cliente.cidade = request.form['cidade']
        cliente.telefone = request.form['telefone']
        cliente.cep = request.form['cep']
        cliente.cpf = request.form['cpf']
        cliente.rg = request.form['rg']
        cliente.habilitacao = request.form['habilitacao']
        cliente.vencimento = request.form['vencimento']
        db.session.commit()
        return redirect(url_for('cadastrar_cliente'))
    return render_template('editar_cliente.html', cliente=cliente)


#Rota para deletar cliente:
@app.route('/delete_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def delete_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for('cadastrar_cliente'))
    return render_template('cadastrar_cliente.html')


#Rota para gerar a ficha de locação:
@app.route('/ficha_locacao', methods=['GET', 'POST'])
def ficha_locacao():
    if request.method == 'POST':
        cliente_id = request.form['cliente']
        carro_id = request.form['carro']
        cliente = Cliente.query.get(cliente_id)
        carro = Carro.query.get(carro_id)

        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
        pdf.drawString(100, 700, f"Cliente: {cliente.nome}")
        pdf.drawString(100, 680, f"Carro: {carro.marca} {carro.modelo}")
        # Adicione mais informações conforme necessário
        pdf.save()

        pdf_buffer.seek(0)  # Volta para o início do buffer

        response = Response(pdf_buffer, content_type='application/pdf')
        response.headers['Content-Disposition'] = 'inline; filename=ficha_locacao.pdf; target=_blank'
        return response

    clientes = Cliente.query.all()
    carros = Carro.query.all()
    return render_template('ficha_locacao.html', clientes=clientes, carros=carros)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    rua = db.Column(db.String(120), nullable=False)
    bairro = db.Column(db.String(120), nullable=False)
    cidade = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(120), nullable=False)
    cep = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(120), nullable=False)
    rg = db.Column(db.String(120), nullable=False)
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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
