from django.shortcuts import render, reverse, redirect
from django.views.generic import FormView, RedirectView
from django.contrib.auth import authenticate,login, logout
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


class LoginView(FormView):
    """This Is the Login class Based View"""
    template_name = 'account/front/login.html'
    form_class = LoginForm


    def form_valid(self,form):
        data = form.cleaned_data
        user = authenticate(email=data['email'],password=data['password'])
        if user.is_active:
            login(self.request,user)
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Succesfully Login.')
        return reverse('main:home')

class LogoutView(RedirectView):
    pattern_name = 'account:login'
    def get(self,request,*args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


