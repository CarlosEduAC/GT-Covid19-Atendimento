from blueprints.menuAtendente import *
from flask_weasyprint import HTML, render_pdf

pdfAgendamento = Blueprint('PdfAgendamento', __name__)

@pdfAgendamento.route('/pdf', methods=['GET'])
@login_required 
def indexPDF():
    template_renderizado = render_template('agendamento.html', atendimentos = getAtendimentos(), formatTime = datetime.strftime, pdf = True, incluiBotaoPdf = False)

    return render_pdf(HTML(string=template_renderizado))

