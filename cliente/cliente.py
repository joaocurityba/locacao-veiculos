from flask import Blueprint, request, redirect, url_for, render_template
from models import Cliente, db


cliente_blueprint = Blueprint('cliente', __name__, template_folder='templates')


#Rota para criar e ler os clientes:
@cliente_blueprint.route('/cadastrar_cliente',  methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        rua = request.form['rua']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        cep = request.form['cep']
        cpf = request.form['cpf']
        identidade = request.form['identidade']
        habilitacao = request.form['habilitacao']
        vencimento = request.form['vencimento']
        new_cliente = Cliente(nome=nome, rua=rua, bairro=bairro, cidade=cidade, telefone=telefone, cep=cep, cpf=cpf, identidade=identidade, habilitacao=habilitacao, vencimento=vencimento)
        db.session.add(new_cliente)
        db.session.commit()
        return redirect(url_for('cliente.cadastrar_cliente'))
    clientes = Cliente.query.all()
    return render_template('cadastrar_cliente.html', clientes=clientes)


#Rota para editar cliente:
@cliente_blueprint.route('/editar_cliente/<int:cliente_id>', methods=['GET', 'POST'])
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
        cliente.identidade = request.form['identidade']
        cliente.habilitacao = request.form['habilitacao']
        cliente.vencimento = request.form['vencimento']
        db.session.commit()
        return redirect(url_for('cliente.cadastrar_cliente'))
    return render_template('editar_cliente.html', cliente=cliente)


#Rota para deletar cliente:
@cliente_blueprint.route('/delete_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def delete_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for('cliente.cadastrar_cliente'))
    return render_template('cadastrar_cliente.html')
