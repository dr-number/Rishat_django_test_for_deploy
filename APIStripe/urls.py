from django.conf.urls import include
from django.urls import path

from APIStripe.views import (
    ProductItem,
    CreateCheckoutSessionView
)


urlpatterns = [
    path('buy/<int:id>/', ProductItem.as_view(), name='buy'),
    path('item/<int:id>/', CreateCheckoutSessionView.as_view(), name='item')
]