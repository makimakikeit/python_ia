from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def hello(request):
    return HttpResponse('<h1>こんにちは</h1>')


def home(request):
    return render(request, 'myapp/home.html')


def mk(request):
    return render(request, 'myapp/mk.html')


class Character:
    def __init__(self, name):
        self.name = name

    def greed(self):
        print(f'{self.name}:こんにちは！')


def home2(request):
    context = {
        'title': 'ホーム２です',
        'message': 'こんにちは、こんばんわ',
        'number_list': [1, 2, 3, 4, 5],
        'user': Character(name = '勇者'), # テンプレートファイルに、インスタンスを渡す
    }
    return render(request, 'myapp/home2.html', context)


# TemplateViewは、htmlを単純に表示するのに使う
class Home(generic.TemplateView):
    # どのテンプレートを使用するかここで書く
    template_name = 'myapp/home2.html'

    # テンプレートファイルに、追加で渡したいデータがある時は
    # このメソッドを呼ぶ
    def get_context_data(self, **kwargs):
        # このメソッド上書きの時は、確実にsupper()で親のメソッドを読んでおく
        context = super().get_context_data(**kwargs)

        # 辞書[キー名] = 値 形式で、追加のデータを渡す
        context['title'] = 'ホーム3です'
        return context


# class Home2(Home): こういうこともできる