from django.db import models
from account.models import Profile
#from django.contrib.auth.models import User
from django.core.files.storage import default_storage

def user_directory_path(instace, filename):
	return 'uploads/imagens/personagens/{0}/{1}'.format(instace.nome, filename)

def user_directory_path_capa(instace, filename):
	return 'uploads/imagens/personagens/capas/{0}'.format(filename)

class Capa(models.Model):
	id 		= models.AutoField(primary_key = True)
	nome 	= models.CharField(max_length = 30)
	imagem	= models.ImageField(upload_to=user_directory_path_capa, blank = False, null = False)
	ativo	= models.BooleanField(blank = False, null = False)

	class Meta:
		verbose_name = u'Capa'
		verbose_name_plural = u'Capas'

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

class Personagem(models.Model):
	id 					= models.AutoField(primary_key = True)
	nome 				= models.CharField(max_length = 30)
	nivel 				= models.DecimalField(max_digits = 5, decimal_places = 0)
	alcunha 			= models.CharField(max_length = 60)
	pontos				= models.DecimalField(max_digits = 19, decimal_places = 0)
	atributos 			= models.TextField()
	vantagens 			= models.TextField()
	desvantagens 		= models.TextField()
	pericias 			= models.TextField()
	peculiaridade 		= models.TextField(blank = True, null = True)
	controle_animais 	= models.TextField(blank = True, null = True)
	turkelva			= models.TextField(blank = True, null = True)
	magias				= models.TextField(blank = True, null = True)
	imagem 				= models.ImageField(upload_to=user_directory_path)
	jogador				= models.ForeignKey(Profile, blank = True, null = True, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name = u'Personagem'
		verbose_name_plural = u'Personagens'

	def save(self, *args, **kwargs):
		if self.id:
		 	old_img = Personagem.objects.get(id=self.id).imagem
		 	default_storage.delete(old_img.path)
			#os.remove(old_img.path)
		elif default_storage.exists(self.imagem.path):
			default_storage.delete(self.imagem.path)

		super(Personagem, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		#default_storage.delete(self.imagem.path)
		self.imagem.delete()
		super(Personagem, self).delete(*args, **kwargs)

	def __unicode__(self): #Python 2
		return self.nome

	def __str__(self): #Python 3
		return self.nome