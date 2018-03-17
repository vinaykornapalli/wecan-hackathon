from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.

class signUp(CreateView):
    form_class = forms.CreateSignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

