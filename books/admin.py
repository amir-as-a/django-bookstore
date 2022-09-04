from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
	list_display = [
		'title',
		'author',
		'price',
	]


class CommentModelAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'book',
		'text',
	]


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Comment, CommentModelAdmin)
