from itertools import count
import stripe
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string

from APIStripe.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

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
                success_url = settings.CURRENT_HOST + '/success/',
                cancel_url = settings.CURRENT_HOST + '/cancel/',
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
            "item" : item,
            "STRIPE_PUBLIC_KEY" : settings.STRIPE_PUBLIC_KEY
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

