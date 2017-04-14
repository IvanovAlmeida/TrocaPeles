from django.shortcuts import render
from .models import Capa
from .models import Mapa

def home(request):

	capa = Capa.objects.get(ativo='1')
	alt  = "Capa TrocaPeles"

	context = {
		'titulo': 'Inicio',
		'capa': capa,
		'alt': alt
	}

	return render(request, 'trocapeles/home.html', context)

def mapa(request):

	imagem = Mapa.objects.get(ativo='1')
	alt = "Mapa de "+imagem.nome

	print(imagem.imagem.url)

	context = {
		'titulo': 'Mapa',
		'mapa': imagem,
		'alt'	: alt,
	}

	return render(request, 'trocapeles/mapa.html', context)