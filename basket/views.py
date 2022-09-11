from django.core.cache import cache
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.template.loader import render_to_string
import json

from APIStripe.models import Item

class Change(View):
    __ADD_TO_BASKET = "1"

    def post(self, request, *args, **kwargs):

        try:

            data_post = json.load(request)
            product_id = data_post["productId"]
            type_change = data_post["typeChange"]

            name_cache = 'product_' + product_id
            count_product = cache.get(name_cache)

            if count_product:
                count_product = int(count_product)
            else:
                count_product = 0


            if type_change == self.__ADD_TO_BASKET:
                count_product += 1
            else:
                count_product -= 1


            if count_product > 0:
                cache.set(name_cache, str(count_product), timeout=None)
            else:
                cache.delete(name_cache)

            return JsonResponse({
                'type': str(type_change),
                'count': str(count_product),
                'status': 'success'
            })

        except Exception as e:
            return JsonResponse({ 
                'error': str(e),
                'status': 'failed'
            })

class Basket(TemplateView):
    template_name = "basket/products.html"

    def get_context_data(self, **kwargs):
        products = Item.objects.all()

        html = ""
        count_type = 0


        for item in products:
            count_product = cache.get('product_' + str(item.id))

            if count_product:
                count_type += 1
                html += render_to_string('basket/item.html', {
                    'item' : item,
                    'count' : count_product
                })


        context = super(Basket, self).get_context_data(**kwargs)
        context.update({
            "products" : html,
            "count_type" : count_type
        })

        return context
