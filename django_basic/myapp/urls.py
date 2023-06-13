from django.urls import path
# .は今いる場所（今回は myapp と書いても実行可能）
from . import views

app_name = 'myapp'

urlpatterns = [
    # どのURLで、どのビュー(処理) を呼ぶか登録する
    # path関数の第一引数は、どのURLか
    # 第二引数が、どのビューを呼ぶか
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('mk/', views.mk, name='mk'),
]