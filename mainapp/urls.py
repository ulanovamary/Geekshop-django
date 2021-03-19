from django.urls import path

from mainapp.views import  products
from adminapp.views import categories_read, categories_create, category_delete, category_update

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:id>/', products, name='product'),
]