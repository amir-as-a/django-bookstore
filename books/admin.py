from django.contrib import admin
from . import models

admin.site.register(models.Book)


class BookAdmin(admin.ModelAdmin):
	list_display = [
		'title',
		'author',
	]
