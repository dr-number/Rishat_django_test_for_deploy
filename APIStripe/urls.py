from django.conf.urls import include
from django.urls import path

from APIStripe.views import (
    Products,
    ProductItem,
    CreateCheckoutSessionView,
    Success,
    Cancel
)


urlpatterns = [
    path('', Products.as_view(), name='products'),
    path('success/', Success.as_view(), name='success'),
    path('cancel/', Cancel.as_view(), name='cancel'),
    path('item/<int:id>/', ProductItem.as_view(), name='buy'),
    path('buy/<int:id>/', CreateCheckoutSessionView.as_view(), name='item')
]