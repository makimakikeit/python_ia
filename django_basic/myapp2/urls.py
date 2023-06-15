from django.urls import path
from . import views

app_name = 'myapp2'
urlpatterns = [
    path('staff_form_input/', views.StaffInformationCreateView.as_view(), name='staff_information_create'),
    path('department_create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('staff_information_create/', views.StaffCreateView.as_view(), name='staff_create'),
    path('staff_list/', views.StaffListView.as_view(), name='staff_list'),
    # データの型：変数名　int型の値がここに埋め込まれて、pkという名前でビューで使用できる
    path('staff_detail/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail')
]
