from django.views import generic
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Article, Tag
from .forms import TagCreateForm, ArticleCreateForm, CategoryCreateForm


class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'


class TagListView(ListView):
    model = Tag  # tag +
    template_name = 'blog/tag_list.html'


class TagCreateView(generic.CreateView):
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = TagCreateForm


class CategoryCreateView(generic.CreateView):
    template_name = 'blog/category_create.html'
    success_url = reverse_lazy('blog:category_list')
    form_class = CategoryCreateForm


class ArticleCreateView(generic.CreateView):
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = ArticleCreateForm

