
import re

from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.core.files.storage import default_storage

def user_directory_path(instace, filename):
	return 'uploads/imagens/users/{0}/avatar/{1}'.format(instace.username, filename)

def get_img_default(instace, filename):
	return 'img/user_avatar.png'

class UserManager(BaseUserManager):

	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not username:
			raise ValueError(_('The given username must be set'))
		email = self.normalize_email(email)
		user = self.model(
					username = username,
					email = email,
					is_staff = is_staff,
					is_active = True,
					is_superuser = is_superuser,
					last_login = now,
					date_joined = now,
					**extra_fields
				)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, username, email=None, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		user=self._create_user(username, email, password, True, True, **extra_fields)
		user.is_active=True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(
		_('username'), 
		max_length = 15, 
		unique = True,
		help_text = _('Required. 15 characters or fewer. Latters, numbers and @/./+/-/_ characters'),
		validators = [
					validators.RegexValidator(
							re.compile('^[\w.@+=]+$'),
							_('Enter a valid username.'),
							_('invalid')
						)
			]
		)
	first_name = models.CharField(_('first name'), max_length = 30)
	last_name = models.CharField(_('last name'), max_length = 30)
	email = models.EmailField(_('email address'), max_length = 255, unique = True)
	is_staff = models.BooleanField(
			_('staff status'),
			default = False,
			help_text = _('Designates whether the user can log into this admin site.')
		)
	is_active = models.BooleanField(
			_('active'),
			default = True,
			help_text = _('Designates wheter this user shold be treated as active. Unselect this instead of deleting accounts.')
		)
	date_joined = models.DateTimeField(_('date joined'), default= timezone.now)
	is_trusty = models.BooleanField(
			_('trusty'),
			default = False,
			help_text = _('Designates wheter this user has confirmed his account.')
		)
	imagem	= models.ImageField(upload_to=user_directory_path, default = 'img/user_avatar.png',blank = False, null = True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

	objects = UserManager()

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])

	# def save(self, *args, **kwargs):
	# 	if self.id:
	# 	 	old_img = User.objects.get(id=self.id).imagem
	# 	 	default_storage.delete(old_img.path)
	# 		#os.remove(old_img.path)
	# 	elif default_storage.exists(self.imagem.path):
	# 		default_storage.delete(self.imagem.path)

	# 	super(User, self).save(*args, **kwargs)

	# def delete(self, *args, **kwargs):
	# 	#default_storage.delete(self.imagem.path)
	# 	self.imagem.delete()
	# 	super(User, self).delete(*args, **kwargs)