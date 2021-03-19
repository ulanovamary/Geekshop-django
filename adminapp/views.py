from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from  authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm, AdminProductCategoryForm

from django.contrib.auth.decorators import user_passes_test

from mainapp.models import Product, ProductCategory
from django.forms import ModelForm


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


#READ
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)

#CREATE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'form': form,
               'title': 'Регистрация', }
    return render(request, 'adminapp/admin-users-create.html', context)


#UPDATE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {
        'form':form,
        'user':user
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)

#DEL
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))

###
#READ
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def categories_read(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/categories-read.html', context)

#CREATE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def categories_create(request):
    if request.method == 'POST':
        form = AdminProductCategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        form = AdminProductCategoryForm()
    context = {'form': form,
               'title': 'Создание категории', }
    return render(request, 'adminapp/categories-create.html', context)


#UPDATE
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def category_update(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = AdminProductCategoryForm(data=request.POST, files=request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        form = AdminProductCategoryForm(instance=category)
    context = {
        'form':form,
        'category':category,
    }
    return render(request, 'adminapp/categories-update-delete.html', context)

#DEL
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def category_delete(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    #category.delete()
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admin_staff:categories'))