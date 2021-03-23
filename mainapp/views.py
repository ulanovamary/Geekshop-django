import os

from django.shortcuts import render
from datetime import datetime

from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'heading': 'geekShop', 'categories': ProductCategory.objects.all(),
               'pages': [{'number': '1'}, {'number': '2'}, {'number': '3'}]}
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)