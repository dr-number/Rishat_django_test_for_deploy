from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy, name='buy'),
    path('item/<int:id>/', views.item, name='item')
]