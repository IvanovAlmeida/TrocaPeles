from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'first_name', 'email', 'is_staff', 'is_active', 'date_joined', 'is_trusty']
	list_editable = ['is_staff', 'is_active']
	search_fields = ['nome', 'username', 'email']
	list_filter = ['is_staff', 'is_active', 'is_trusty']

admin.site.register(User, UserAdmin)