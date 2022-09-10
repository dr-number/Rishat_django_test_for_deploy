from django.conf.urls import include
from django.urls import path

from APIStripe.views import (
    ProductItem,
    CreateCheckoutSessionView
)


urlpatterns = [
    path('item/<int:id>/', ProductItem.as_view(), name='buy'),
    path('buy/<int:id>/', CreateCheckoutSessionView.as_view(), name='item')
]