from flask import Flask, render_template
from models import db
from carro.carro import carro_blueprint
from cliente.cliente import cliente_blueprint
from locacao.locacao import locacao_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#Inicialização do DB com o atributo 'app':
db.init_app(app)

#Registro dos Blueprints:
app.register_blueprint(carro_blueprint)
app.register_blueprint(cliente_blueprint)
app.register_blueprint(locacao_blueprint)


#Rota Index:
@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
    