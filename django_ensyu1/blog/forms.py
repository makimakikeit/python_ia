from django import forms
from .models import Tag, Article, Category


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        # ページに表示したり、モデルのフィールドを文字列で書きます
        fields = ('name', )


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        # ページに表示したり、モデルのフィールドを文字列で書きます
        fields = ('name', )


class ArticleCreateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'created_at', 'category', 'tags')