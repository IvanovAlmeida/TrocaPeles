from django.shortcuts import render
from var_dump import var_dump

from .models import Personagem, Capa

def index(request):
	#Pega Capa da VIEW
	if Capa.objects.filter(ativo='1'):
		capa = Capa.objects.get(ativo='1')
	else:
		capa = False

	if Personagem.objects.exists():
		personagens = Personagem.objects.values('nome', 'nivel', 'jogador__username')

	else:
		personagens = False

	context = {
		'titulo': "Personagens",
		'capa': capa,
		'alt': "Capa Personagens",
		'personagens': personagens,
	}

	return render(request, 'personagens/index.html', context)
