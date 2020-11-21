from django.shortcuts import render
from . import forms
from django.views.generic import FormView
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
import requests

# Create your views here.


class TicketFormView(FormView):
    template_name = 'ticket/ticket.html'
    form_class = forms.TicketForm

    def get_success_url(self):
        messages.success(self.request,'Your Ticket is successfully Rised')
        return HttpResponseRedirect('add_ticket')

    def form_valid(self,form):
        data = form.cleaned_data
        print(data)
        return super().form_valid(form)

