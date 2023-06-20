from django.views import generic
from django.urls import reverse_lazy
from .forms import MyUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    # next_page = '/accounts/login/'
    # ログアウト後に、移動するページ
    next_page = reverse_lazy('accounts:login')


class Home(TemplateView):
    template_name = 'accounts/home.html'


# class Home(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'accounts/home.htl'


class AccountCreateView(generic.CreateView):
    Model = CustomUser
    form_class = MyUserCreationForm  # つくったフォームを指定する
    # form_class = UserCreationForm  # ユーザー作成するための、提供されているフォーム
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')