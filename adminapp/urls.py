from django.urls import path

from adminapp.views import (index, admin_users, admin_users_update, admin_users_create, admin_users_delete, category_update,  category_delete, categories_create, categories_read)
#if import extends 120 symbols, then cover it with parentheses

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:user_id>', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:user_id>', admin_users_delete, name='admin_users_delete'),

    path('categories/create/', categories_create, name='category_create'),
    path('categories/read/', categories_read, name='categories'),
    path('categories/update/<int:category_id>/', category_update, name='category_update'),
    path('categories/delete/<int:category_id>/', category_delete, name='category_delete'),

]