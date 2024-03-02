from flask import Blueprint, request, render_template, Response
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from models import Cliente, Carro


locacao_blueprint = Blueprint('locacao', __name__, template_folder='templates')


#Rota para gerar a ficha de locação:
@locacao_blueprint.route('/ficha_locacao', methods=['GET', 'POST'])
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
