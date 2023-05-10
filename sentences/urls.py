from django.urls import path
from sentences import views

urlpatterns = [
    path('',views.taqvim ,name='home')
]