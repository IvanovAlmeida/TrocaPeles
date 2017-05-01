from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instace, filename):
	return 'uploads/imagens/usuarios/{0}/avatar/{1}'.format(instace.user.username, filename)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to=user_directory_path, default='/')

	class Meta:
		verbose_name = u'Perfil'
		verbose_name_plural = u'Perfis'