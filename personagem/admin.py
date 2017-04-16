from django.contrib import admin
from .models import Personagem, Capa

class PersonagemAdmin(admin.ModelAdmin):
	list_display = ['nome', 'jogador', 'nivel', 'pontos']
	list_editable = ['nivel', 'pontos']
	search_fields = ['nome']

admin.site.register(Personagem, PersonagemAdmin)

class CapaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'imagem', 'ativo']
	search_fields = ['nome']

admin.site.register(Capa, CapaAdmin)