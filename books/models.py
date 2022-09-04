from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
	title = models.CharField(max_length = 100, blank = True)
	author = models.CharField(max_length = 100, blank = True)
	description = models.TextField(blank = True)
	price = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
	image = models.ImageField(upload_to = 'cover/', blank = True)
	
	def __str__(self):
		return f'{self.title}'
	
	def get_absolute_url(self):
		return reverse('book_detail', args = [self.id])


class Comment(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	text = models.TextField()
	insertTime = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'{self.user}:{self.text}'
