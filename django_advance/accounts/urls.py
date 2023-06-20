from django.urls import path
from . import views
# ログイン必須にする
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('accounts_create/', views.AccountCreateView.as_view(), name='create'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Login.as_view(), name='logout'),
    # ページをログイン必須にする。『login_required』をつける
    path('home/', login_required(views.Home.as_view()), name='home'),

]