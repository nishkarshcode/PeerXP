from django.shortcuts import render
from django.views.generic import FormView
from account.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.shortcuts import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def index_page(request):
    return render(request,'main/front/index.html',{})

class LoginView(FormView):
    """This Is the Login class Based View"""
    template_name = 'main/front/index.html'
    form_class = LoginForm


    def form_valid(self,form):
        data = form.cleaned_data
        user = authenticate(email=data['email'],password=data['password'])
        if user.is_active:
            login(self.request,user)
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('main:home')



    
    
