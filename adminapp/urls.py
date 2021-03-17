from django.urls import path

from adminapp.views import (index, admin_users, admin_users_update, admin_users_create, admin_users_delete)
#if import extends 120 symbols, then cover it with parentheses

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:user_id>', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:user_id>', admin_users_delete, name='admin_users_delete')

    #path('categories/create/', adminapp.category_create, name='category_create'),
    #path('categories/read/', adminapp.categories, name='categories'),
    #path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    #path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

]