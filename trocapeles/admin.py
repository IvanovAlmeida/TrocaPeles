from django.contrib import admin
from .models import Mapa
from .models import Capa

class CapaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'imagem', 'ativo']
	search_fields = ['nome']

admin.site.register(Capa, CapaAdmin)

class MapaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'imagem', 'ativo']
	search_fields = ['nome']

admin.site.register(Mapa, MapaAdmin)