from django.shortcuts import render
from datetime import datetime

# функции = вьюхи = контроллеры
def index(request):
    context = {
        'title': 'geekShop',
        'heading':'geekShop store',
        'text': 'Новые образы и лучшие бренды на GeekShop Store. '
                'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'date': datetime
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekShop - Каталог',
        'heading': 'geekShop',
        'goods': [
            {'picture': 'vendor/img/products/Adidas-hoodie.png', 'name': 'Худи черного цвета с монограммами adidas Originals', 'price':'6 090,00', 'text':'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'picture': 'vendor/img/products/Blue-jacket-The-North-Face.png', 'name': 'Синяя куртка The North Face', 'price': '23 725,00', 'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'picture': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00', 'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'picture': 'vendor/img/products/Black-Nike-Heritage-backpack.png', 'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00', 'text': 'Плотная ткань. Легкий материал.'},
            {'picture': 'vendor/img/products/Black-Dr-Martens-shoes.png', 'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00', 'text': 'Гладкий кожаный верх. Натуральный материал.'},
            {'picture': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00', 'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],
        'categories_list': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'}
        ],
        'pages':[
            {'number': '1'},
            {'number': '2'},
            {'number': '3'},
        ],
    }
    return render(request, 'mainapp/products.html', context)