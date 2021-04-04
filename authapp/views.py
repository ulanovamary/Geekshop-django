from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from authapp.forms import UserLoginForm, UserCreationForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required

from geekshop import settings

from authapp.models import User



def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('main'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form':form,
               'title':'Авторизация',
               }
    return render(request,'authapp/login.html', context)

class RegisterViewForm(FormView):
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

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form':form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)