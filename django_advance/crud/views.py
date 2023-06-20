from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm


class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create'


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods
    template_name = 'crud/goods_detail.html'


class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = reverse_lazy('crud:goods_create')


class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'

    def form_valid(self, form):
        # 削除処理を変更するために、メソッド上書き
        # リダイレクト先のURLを取得
        success_url = self.get_success_url()

        # モデルインスタンス.フィールド名 = 値 で、書き換えや代入ができます
        self.object.state_flag = False
        # saveメソッドで、DBのレコードの更新や作成ができる
        self.object.save()
        # self.object.delete()  # これが本来の削除処理
        return redirect(success_url)

