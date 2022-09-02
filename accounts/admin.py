from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import form, models


class CustomUserAdmin(UserAdmin):
	add_form = form.CustomUserCreationForm
	form = form.UserChangeForm
	model = models.CustomUser
	list_display = ['username', 'age', 'email', 'is_staff']
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('age',)}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('age',)}),
	
	)


admin.site.register(models.CustomUser, CustomUserAdmin)
