from authapp.forms import UserRegisterForm, UserProfileForm
from mainapp.models import ProductCategory
from authapp.models import User
from django import forms
from django.forms import ModelForm
from django.db import models



class UserAdminRegistrationForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(UserAdminRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class AdminProductCategoryForm(ModelForm):
    is_active = models.BooleanField(('active'),default=True)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_active')
    form = ProductCategory()

    def __init__(self, *args, **kwargs):
        super(AdminProductCategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

