import stripe
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        try:
            session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                        'name': 'T-shirt',
                        },
                        'unit_amount': 2000,
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



class ProductItem(TemplateView):
    template_name: "APIStripe/item.html"

