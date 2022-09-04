from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
	list_display = [
		'title',
		'author',
		'price',
	]


admin.site.register(models.Book, BookAdmin)
