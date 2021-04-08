from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, UpdateView

from authapp.forms import UserLoginForm, UserCreationForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required

from geekshop import settings

from authapp.models import User, UserProfile

from django.db import transaction
from authapp.forms import UserProfileEditForm



# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form':form,
#                'title':'Авторизация',
#                }
#     return render(request,'authapp/login.html', context)
class Login(LoginView):
    model = User
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'authapp/login.html'
    title = 'Login'


class RegisterView(FormView):
    model = User
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_mail(user):
                messages.success(request, 'Вы успешно зарегистрированы! Активируйте Вашу учетную запись по e-mail.')
                return redirect(self.success_url)
            return redirect(self.success_url)

        return render(request, self.template_name, {'form':form})


    def send_verify_mail(self, user):
       verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
       title = f'Подтверждение учетной записи {user.username}'

       message = f'Для подтверждения учетной записи {user.username} на портале \
       {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
       return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


    def verify(request, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user.activation_key == activation_key and not user.is_activation_key_expired():
                user.is_active = True
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(request, 'authapp/verification.html')
            else:
                print(f'error activation user: {user}')
                return render(request, 'authapp/verification.html')
        except Exception as e:
            print(f'error activation user : {e.args}')
            return HttpResponseRedirect(reverse('main'))


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             if send_verify_mail(User):
#                 messages.success(request, 'Вы успешно зарегистрированы!')
#                 return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         form = UserRegisterForm()
#     context = {'form':form,
#                'title':'Регистрация',}
#     return render(request, 'authapp/register.html', context)


 # def logout(request):
 #     auth.logout(request)
 #     return HttpResponseRedirect(reverse('index'))

class Logout (LogoutView):
    template_name = 'authapp/login.html'


class LoginRequireMixin(object):
    pass


class ProfileEdit(LoginRequireMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    form_class_second = UserProfileEditForm
    success_url = reverse_lazy('auth:profile')
    template_name = 'authapp/profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileEdit, self).get_context_data(**kwargs)

        self_pk = self.object.pk
        user = User.objects.get(pk=self_pk)
        context['profile_form'] = self.form_class_second(instance=user.userprofile)
        context['baskets'] = Basket.objects.filter(user=user)
        return context


@transaction.atomic
def post(self, request, *args, **kwargs):
    user = User.objects.get(pk=self.request.user.pk)
    edit_form = UserProfileForm(data=request.POST, files=request, instance=user)
    profile_form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=user.userprofile)

    if edit_form.is_valid() and profile_form.is_valid():
        edit_form.save()
        user.userprofile.save()
        return HttpResponseRedirect(self.success_url)

    return render(request, self.template_name,{
        'form':edit_form,
        'profile_form':profile_form,
    })

# def edit(request):
#     title = 'редактирование'
#
#     if request.method == 'POST':
#         edit_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         profile_form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.userprofile)
#
#         if edit_form.is_valid() and profile_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('auth:profile'))
#     else:
#         edit_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         profile_form = UserProfileEditForm(data=request.POST, files=request.FILES,
#                                                instance=request.user.userprofile)
#     context = {
#         'title': title,
#         'edit_form':edit_form,
#         'profile_form':profile_form
#         }
#     return render(request, 'authapp/profile.html', context)context