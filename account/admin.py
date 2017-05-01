from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline, )
	list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ['nome', 'jogador', 'nivel', 'pontos']
# 	list_editable = ['nivel', 'pontos']
# 	search_fields = ['nome']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)