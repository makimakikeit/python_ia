from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm, StaffInformationUpdateForm


class StaffDetailView(generic.DetailView):
    model = Staff
    template_name = 'myapp2/staff_detail.html'

    # DetailViewがもともと持っている、get_objectメソッドの紹介。データベースから、1つのデータを取得する
    def get_object(self, queryset=None):
        # self.kwargsは、URL内の int:pkといった部分が入っている
        staff = Staff.objects.get(pk=self.kwargs['pk'])
        # →Staff.objects.get(pk=1)  # 今回、URLは/staff_detail/1/
        # →Staff.objects.get(id=1)  # pkというのは、primarykeyのこと。今回ならidフィールドのこと
        return staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # DetailViewにはget.objectメソッドがあり、
        # URLのidを元に、モデルのインスタンスを取得している
        staff = self.get_object()
        context['books'] = staff.rented_books.all()
        return context


class StaffListView(generic.ListView):
    # どのモデルを使用するのか
    model = Staff
    # どこから表示する情報を取ってくるか
    template_name = 'myapp2/staff_list.html'


class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'
    # 処理が成功した場合の、リダイレクト先
    # 追加・削除・更新は、処理の後にリダイレクトするのが普通
    success_url = reverse_lazy('myapp:home')


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'myapp2/department_create.html'
    # URLの逆引きを行う app_name:path関数のname
    success_url = reverse_lazy('myapp:home')
    # 結果的に次のようになる
    # success_url = '/home/'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp2/book_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffInformationUpdateView(generic.UpdateView):
    model = StaffInformation
    form_class = StaffInformationUpdateForm
    template_name = 'myapp2/staff_information_update.html'
    success_url = reverse_lazy('myapp:home')