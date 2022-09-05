from django.urls import reverse_lazy, reverse
from django.views import generic
from . import models, forms
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class BookListView(generic.ListView):
	model = models.Book
	paginate_by = 4
	template_name = 'book/book_list.html'
	context_object_name = 'all_book'


# class BookDetailView(generic.DetailView):
# 	model = models.Book
# 	template_name = 'book/book_detail.html'
# 	context_object_name = 'book'
@login_required
def book_detail_view(request, pk):
	books = get_object_or_404(models.Book, pk = pk)
	comments = books.comments.filter(is_active = True)
	if request.method == 'POST':
		comment_form = forms.CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit = False)
			new_comment.book = books
			new_comment.user = request.user
			new_comment.save()
			comment_form = forms.CommentForm()
	else:
		comment_form = forms.CommentForm()
	
	return render(request, 'book/book_detail.html', {
		'book': books,
		'comment_form': comment_form,
		'comments' : comments,
	})


class BookCreateView(LoginRequiredMixin, generic.CreateView):
	form_class = forms.BookForm
	template_name = 'book/add_book.html'


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
	model = models.Book
	form_class = forms.BookForm
	template_name = 'book/add_book.html'


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
	model = models.Book
	template_name = 'book/delete_book.html'
	success_url = reverse_lazy('book_list')
