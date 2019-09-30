import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.views.generic import (
	ListView,
	UpdateView,
	DeleteView,
	CreateView
)
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.views import View


class UsuariosList(ListView):
	model = Usuario

	def get_queryset(self):
		programa_logado = self.request.user.usuario.programa
		return Usuario.objects.filter(programa=programa_logado)

class UsuariosEdit(UpdateView):
	model = Usuario
	fields = ['nome', 'clienteassociado']

class UsuariosDelete(DeleteView):
	model = Usuario
	success_url = reverse_lazy('list_usuarios')

class UsuariosNovo(CreateView):
	model = Usuario
	fields = ['nome', 'clienteassociado']

	def form_valid(self, form): #interessante inserir uma cláusula if para usuários com sobrenomes iguais.
		usuario = form.save(commit=False) # salva na memória mas não joga para o BD
		username = usuario.nome.split(' ')[0] + usuario.nome.split(' ')[1]
		usuario.programa = self.request.user.usuario.programa
		usuario.user = User.objects.create(username=username)
		usuario.save()
		return super(UsuariosNovo, self).form_valid(form)

def pdf_reportlab(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = "attachment; filename=meupdf.pdf"

	buffer = io.BytesIO()
	p = canvas.Canvas(buffer)
	p.drawString(10, 810, "Relatorio de Funcionarios")

	usuarios = Usuario.objects.filter(programa=request.user.usuario.programa)

	str01 = 'Nome: %s | Usuário: %s'

	y = 790

	for usuario in usuarios:
		p.drawString(10, y, str01 % (usuario.nome, usuario.user))
		y -=40

	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response

class Render:

	@staticmethod
	def render(path: str, params: dict, filename: str):
		template = get_template(path)
		html = template.render(params)
		response = io.BytesIO()
		pdf = pisa.pisaDocument(
			io.BytesIO(html.encode("UTF-8")), response)
		if not pdf.err:
			response = HttpResponse(
				response.getvalue(), content_type='application/pdf')
			response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
			return response
		else:
			return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

	def get(self, request):
		params = {
		'today': 'Variavel today',
		'sales': 'Variavel sales',
		'request': request,
		}
		return Render.render('usuarios/relatorio.html', params, 'myfile')
