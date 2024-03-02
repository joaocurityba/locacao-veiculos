from flask import Blueprint, request, redirect, url_for, render_template
from models import Carro, db


carro_blueprint = Blueprint('carro', __name__, template_folder='templates')


#Create and Read:
@carro_blueprint.route('/cadastrar_carro', methods=['GET', 'POST'])
def cadastrar_carro():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        placa = request.form['placa']
        chassi = request.form['chassi']
        cor = request.form['cor']
        combustivel = request.form['combustivel']
        new_car = Carro(marca=marca, modelo=modelo, ano=ano, placa=placa, chassi=chassi, cor=cor, combustivel=combustivel)
        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for('carro.cadastrar_carro'))
    all_users = Carro.query.all()
    return render_template('cadastrar_carro.html', carros=all_users)


#Delete:
@carro_blueprint.route('/delete_carro/<int:carro_id>', methods=['GET', 'POST'])
def delete_carro(carro_id):
    carro = Carro.query.get(carro_id)
    if carro:
        db.session.delete(carro)
        db.session.commit()
        return redirect(url_for('carro.cadastrar_carro'))
    return render_template('cadastrar_carro.html')


#Update:
@carro_blueprint.route('/editar_carro/<int:carro_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('carro.cadastrar_carro'))
    return render_template('editar_carro.html', carro=carro)
