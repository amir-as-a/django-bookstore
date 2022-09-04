from django.test import TestCase
from django.urls import reverse
from . import models
from decimal import *


class BookTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.book1 = models.Book.objects.create(
			title = 'book',
			author = 'amir',
			description = 'test des',
			price = 19,
		)
		
		cls.book2 = models.Book.objects.create(
			title = 'book 01',
			author = 'amir 01',
			description = 'test des 01',
			price = 11.99,
		)
	
	def test_book_list_url(self):
		response = self.client.get('/book/')
		self.assertEqual(response.status_code, 200)
	
	def test_book_list_by_name(self):
		response = self.client.get(reverse('book_list'))
		self.assertEqual(response.status_code, 200)
	
	def test_book_list_content(self):
		response = self.client.get(reverse('book_list'))
		self.assertContains(response, self.book1.title)
		self.assertContains(response, self.book1.description)
		self.assertContains(response, self.book1.author)
		self.assertContains(response, self.book1.price)
	
	def test_book_detail_url(self):
		response = self.client.get(f'/book/{self.book1.id}/')
		self.assertEqual(response.status_code, 200)

	def test_book_detail_by_name(self):
		response = self.client.get(reverse('book_detail', args =[self.book1.id]))
		self.assertEqual(response.status_code, 200)
	
	def test_book_detail_content(self):
		response = self.client.get(reverse('book_detail', args = [self.book1.id]))
		self.assertContains(response, self.book1.title)
		self.assertContains(response, self.book1.description)
		self.assertContains(response, self.book1.author)
		self.assertContains(response, self.book1.price)

	def test_book_create(self):
		response = self.client.post(reverse('add_book'), {
			'title': 'book 3',
			'author': 'Arsalan 3',
			'description': 'test des 3',
			'price': 13.99
		})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(models.Book.objects.last().title, 'book 3')
		self.assertEqual(models.Book.objects.last().author, 'Arsalan 3')
		self.assertEqual(models.Book.objects.last().description, 'test des 3')
		self.assertEqual(models.Book.objects.last().price, Decimal('13.99'))
		
	def test_book_update(self):
		response = self.client.post(reverse('update_book', args = [self.book2.id]), {
			'title': 'book 2',
			'author': 'Arsalan 2',
			'description': 'test des 2',
			'price': 12.99
		})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(models.Book.objects.last().title, 'book 2')
		self.assertEqual(models.Book.objects.last().author, 'Arsalan 2')
		self.assertEqual(models.Book.objects.last().description, 'test des 2')
		self.assertEqual(models.Book.objects.last().price, Decimal('12.99'))
		
	def test_book_delete(self):
		response = self.client.post(reverse('delete_book', args = [self.book2.id]))
		self.assertEqual(response.status_code, 302)