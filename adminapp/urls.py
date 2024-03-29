from django.urls import path

from adminapp.views import (index, UserListView, UserUpdateView, UserCreateView, UserDeleteView, CategoryUpdateView,  CategoryDeleteView, CategoryCreateView, CategoryListView, ProductCreateView, ProductListView, product_delete, ProductUpdateView)
#if import extends 120 symbols, then cover it with parentheses

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', CategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/read/', ProductListView.as_view(), name='products'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:product_id>/', product_delete, name='product_delete'),

]