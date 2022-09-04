from django.urls import reverse_lazy
from django.views import generic
from . import models, forms


class BookListView(generic.ListView):
	model = models.Book
	paginate_by = 4
	template_name = 'book/book_list.html'
	context_object_name = 'all_book'


class BookDetailView(generic.DetailView):
	model = models.Book
	template_name = 'book/book_detail.html'
	context_object_name = 'book'


class BookCreateView(generic.CreateView):
	form_class = forms.BookForm
	template_name = 'book/add_book.html'


class BookUpdateView(generic.UpdateView):
	model = models.Book
	form_class = forms.BookForm
	template_name = 'book/add_book.html'


class BookDeleteView(generic.DeleteView):
	model = models.Book
	template_name = 'book/delete_book.html'
	success_url = reverse_lazy('book_list')
