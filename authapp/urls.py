from django.urls import path

from authapp.views import login, RegisterViewForm, logout, profile, verify

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', RegisterViewForm.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    #path('<int:id>/', products, name='product'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]