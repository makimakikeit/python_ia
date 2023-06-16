from django import forms
from .models import StaffInformation, Department, Book, Staff


class StaffInformationForm(forms.ModelForm):
    # jango では class Meta: を定義する必要がある
    class Meta:
        model = StaffInformation
        # 画面上に表示する入力覧に対応している
        # fields = '__all__'
        # excludes = ('email')
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'management_code')


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'information', 'department', 'rented_books')


class StaffInformationUpdateForm(forms.ModelForm):

    class Meta:
        model = StaffInformation
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')