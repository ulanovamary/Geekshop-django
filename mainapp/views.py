import json
import os

from django.shortcuts import render
from datetime import datetime

from mainapp.models import Product, ProductCategory

dir = os.path.dirname(__file__)


# функции = вьюхи = контроллеры
def index(request):
    context = {
        'title': 'geekShop',
        'heading': 'geekShop store',
        'text': 'Новые образы и лучшие бренды на GeekShop Store. '
                'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'date': datetime
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'geekShop - Каталог',
        'heading': 'geekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'pages': [
            {'number': '1'},
            {'number': '2'},
            {'number': '3'},
        ],
    }

    return render(request, 'mainapp/products.html', context)
