from django.db import models
from django.urls import reverse


class Book(models.Model):
	title = models.CharField(max_length = 100, blank = True)
	author = models.CharField(max_length = 100, blank = True)
	description = models.TextField(blank = True)
	
	def __str__(self):
		return f'{self.title}'
	
	def get_absolute_url(self):
		return reverse('book_detail', args = [self.id])
