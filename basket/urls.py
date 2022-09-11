from django.conf.urls import include
from django.urls import path
from APIStripe.views import BasketCreateCheckoutSessionView

from basket.views import (
    Change,
    Basket
    )


urlpatterns = [
    path('', Basket.as_view(), name='basket'),
    path('change', Change.as_view(), name='basket_change'),
    path('buy_basket', BasketCreateCheckoutSessionView.as_view(), name='buy_basket')
]