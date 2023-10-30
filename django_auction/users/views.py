from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserProfileForm, UserRegistrationForm, UserLoginForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Login'

    def get_success_url(self):
        return reverse_lazy('index')


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зареганы'
    title = 'Store - Registration'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form = UserProfileForm
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Profile'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))



def logout(request):
    auth.logout(request)
    return redirect('index')
