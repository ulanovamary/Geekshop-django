from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm, AdminProductCategoryForm, AdminProductForm

from django.contrib.auth.decorators import user_passes_test

from mainapp.models import Product, ProductCategory

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


#READ
class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    queryset = User.objects.all() #передать праметры отображение, например только активных

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)
#@user_passes_test(lambda u: u.is_superuser, login_url='/')
#def admin_users(request):
#    context = {
#        'users': User.objects.all()
#    }
#    return render(request, 'adminapp/admin-users-read.html', context)

#CREATE
class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')


# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'form': form,
#                'title': 'Регистрация', }
#     return render(request, 'adminapp/admin-users-create.html', context)


#UPDATE
class UserUpdateView(UpdateView):
    model = User
    template_name ='adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admin_staff:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context


# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def admin_users_update(request, user_id):
#     user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user)
#     context = {
#         'form':form,
#         'user':user
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

#DEL
class UserDeleteView(DeleteView):
    model = User
    template_name ='adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def admin_users_delete(request, user_id):
#     user = User.objects.get(id=user_id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))

###
#READ category
class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories-read.html'
    queryset = ProductCategory.objects.all() #передать праметры отображение, например только активных

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def categories_read(request):
#     context = {
#         'categories': ProductCategory.objects.all()
#     }
#     return render(request, 'adminapp/categories-read.html', context)

#CREATE category
class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/categories-create.html'
    form_class = AdminProductCategoryForm
    success_url = reverse_lazy('admin_staff:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def categories_create(request):
#     if request.method == 'POST':
#         form = AdminProductCategoryForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#     else:
#         form = AdminProductCategoryForm()
#     context = {'form': form,
#                'title': 'Создание категории', }
#     return render(request, 'adminapp/categories-create.html', context)


#UPDATE category
class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/categories-update-delete.html'
    form_class = AdminProductCategoryForm
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args , **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def category_update(request, category_id):
#     category = ProductCategory.objects.get(id=category_id)
#     if request.method == 'POST':
#         form = AdminProductCategoryForm(data=request.POST, files=request.FILES, instance=category)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#     else:
#         form = AdminProductCategoryForm(instance=category)
#     context = {
#         'form':form,
#         'category':category,
#     }
#     return render(request, 'adminapp/categories-update-delete.html', context)

#DEL category

class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name ='adminapp/categories-update-delete.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование категории'
        return context

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def category_delete(request, category_id):
#     category = ProductCategory.objects.get(id=category_id)
#     #category.delete()
#     category.is_active = False
#     category.save()
#     return HttpResponseRedirect(reverse('admin_staff:categories'))


###
#READ product

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products-read.html'
    queryset = Product.objects.all()  # передать праметры отображение, например только активных

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def products_read(request):
#     context = {
#         'products': Product.objects.all()
#     }
#    return render(request, 'adminapp/products-read.html', context)

#CREATE product

class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/products-create.html'
    form_class = AdminProductForm
    success_url = reverse_lazy('admin_staff:products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def product_create(request):
#     if request.method == 'POST':
#         form = AdminProductForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products'))
#     else:
#         form = AdminProductForm()
#     context = {'form': form,
#                'title': 'Создание продукта', }
#     return render(request, 'adminapp/products-create.html', context)

#UPDATE product

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/products-update-delete.html'
    form_class = AdminProductForm
    success_url = reverse_lazy('admin_staff:products')

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args , **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def product_update(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == 'POST':
#         form = AdminProductForm(data=request.POST, files=request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products'))
#     else:
#         form = AdminProductForm(instance=product)
#     context = {
#         'form':form,
#         'product':product,
#     }
#     return render(request, 'adminapp/products-update-delete.html', context)
#


#DEL product


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_staff:products'))