from django.urls import path
from . import views

#Code from here
app_name ="ticket"

urlpatterns = [
    path('add-ticket',views.TicketFormView.as_view(),name='add_ticket'),    
]
