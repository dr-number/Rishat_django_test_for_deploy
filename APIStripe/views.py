from array import array
from itertools import count
import stripe
from django.conf import settings
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.cache import cache
import json


from APIStripe.models import Item
from main.functions import getCurrentHost

stripe.api_key = settings.STRIPE_SECRET_KEY

class BasketCreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):

        try:
            data_post = json.load(request)

            session = stripe.checkout.Session.create(
                line_items = data_post['data'],
                mode = 'payment',
                success_url = getCurrentHost(request) + 'success/',
                cancel_url = getCurrentHost(request) + 'cancel/',
            )

            clears = []

            ids = data_post['ids']

            for id in ids:
                clears.append('product_' + id)

            cache.delete_many(clears)


            return JsonResponse({
                'id': session.id
            })

        except Exception as e:
            return JsonResponse({ 
                'error': str(e)
            })


class CreateCheckoutSessionView(View):
    def get(self, request, id, *args, **kwargs):

        item = Item.objects.get(pk = id)

        try:
            session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                        'name': item.name,
                        },
                        'unit_amount': round(item.price * 100),
                    },
                    'quantity': 1,
                }],
                mode = 'payment',
                success_url = getCurrentHost(request) + 'success/',
                cancel_url = getCurrentHost(request) + 'cancel/',
            )

            return JsonResponse({
                'id': session.id
            })

        except Exception as e:
            return JsonResponse({ 
                'error': str(e)
            })


class Success(TemplateView):
    template_name = "APIStripe/success.html"

class Cancel(TemplateView):
    template_name = "APIStripe/cancel.html"


class ProductItem(TemplateView):
    template_name = "APIStripe/item.html"

    def get(self, request, id, *args, **kwargs):
        item = Item.objects.get(pk = id)

        context = super(ProductItem, self).get_context_data(**kwargs)
        context.update({
            "item" : item
        })

        return context


class Products(TemplateView):
    template_name = "APIStripe/products.html"

    def get_context_data(self, **kwargs):
        products = Item.objects.all()

        html = ""

        for item in products:
            html += render_to_string('APIStripe/item.html', {
                'item' : item
            })

        context = super(Products, self).get_context_data(**kwargs)
        context.update({
            "products" : html,
            "count" : products.count()
        })

        return context

