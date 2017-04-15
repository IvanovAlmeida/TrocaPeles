from django.shortcuts import render
from .models import Capa
from .models import Mapa

def home(request):

	if Capa.objects.filter(ativo='1'):
		capa = Capa.objects.get(ativo='1')
	else:
		capa = False
	
	alt  = "Capa TrocaPeles"
	context = {
		'titulo': 'Inicio',
		'capa': capa,
		'alt': alt
	}

	return render(request, 'trocapeles/home.html', context)

def mapa(request):

	if Mapa.objects.filter(ativo='1'):
		mapa = Mapa.objects.get(ativo='1')
		alt = "Mapa de "+mapa.nome
	else:
		mapa = False
		alt	= "Mapa"	

	context = {
		'titulo': 'Mapa',
		'mapa': mapa,
		'alt'	: alt,
	}

	return render(request, 'trocapeles/mapa.html', context)