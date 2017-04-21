from django.shortcuts import render, get_object_or_404

from .models import Personagem, Capa

def index(request):
	#Pega Capa da VIEW
	if Capa.objects.filter(ativo='1'):
		capa = Capa.objects.get(ativo='1')
	else:
		capa = False

	if Personagem.objects.exists():
		#personagens = Personagem.objects.values('id', 'nome', 'nivel', 'jogador__username', 'jogador__imagem__url')
		personagens = Personagem.objects.all()

	else:
		personagens = False

	context = {
		'titulo': "Personagens",
		'capa': capa,
		'alt': "Capa Personagens",
		'personagens': personagens,
	}

	return render(request, 'personagens/index.html', context)

def view(request, id):
	personagem = get_object_or_404(Personagem, id=id)

	context = {
		'titulo' : personagem.nome,
		'personagem': personagem
	}

	return render(request, 'personagens/view.html', context)