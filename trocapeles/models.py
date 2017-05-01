from django.db import models

def user_directory_path_mapa(instace, filename):
	return 'uploads/imagens/mapas/{0}'.format(filename)

def user_directory_path_capa(instace, filename):
	return 'uploads/imagens/capa/{0}'.format(filename)
	
class Capa(models.Model):
	id 		= models.AutoField(primary_key = True)
	nome 	= models.CharField(max_length = 30)
	imagem	= models.ImageField(upload_to=user_directory_path_capa, blank = False, null = False)
	ativo	= models.BooleanField(blank = False, null = False)

	def __unicode__(self): #Python 2
		return self.nome

	def __str__(self): #Python 3
		return self.nome

	def save(self, *args, **kwargs):

		if self.ativo and Capa.objects.filter(ativo='1').count():
			old_ativo = Capa.objects.get(ativo='1')
			old_ativo.ativo = 0
			old_ativo.save()

		super(Capa, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		#self.imagem.delete()
		default_storage.delete(self.imagem.path)
		super(Capa, self).delete(*args, **kwargs)

class Mapa(models.Model):
	id 		= models.AutoField(primary_key = True)
	nome 	= models.CharField(max_length = 30) 
	imagem 	= models.ImageField(upload_to=user_directory_path_mapa, blank = False, null = False)
	ativo	= models.BooleanField(blank = False, null = False)

	def __unicode__(self): #Python 2
		return self.nome

	def __str__(self): #Python 3
		return self.nome

	def save(self, *args, **kwargs):

		if self.ativo and Mapa.objects.filter(ativo='1').count():
			old_ativo = Mapa.objects.get(ativo='1')
			old_ativo.ativo = 0
			old_ativo.save()

		super(Mapa, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		#self.imagem.delete()
		default_storage.delete(self.imagem.path)
		super(Mapa, self).delete(*args, **kwargs)