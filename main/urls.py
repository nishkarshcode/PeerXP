from django.urls import path
from . import views


#Code from here

app_name='main'

urlpatterns = [
    path('',views.index_page,name="home"),
]
