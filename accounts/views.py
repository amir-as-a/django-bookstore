from django.shortcuts import render
from django.views import generic
from . import form
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
	form_class = form.CustomUserCreationForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('login')
	