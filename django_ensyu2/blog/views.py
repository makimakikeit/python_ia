from django.views import generic
from django.urls import reverse_lazy
from .forms import TagCreateForm, ArticleCreateForm, ArticleUpdateForm
from .models import Article, Tag



class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'


class TagListView(generic.ListView):
    model = Tag  # tag  + _list
    template_name = 'blog/tag_list.html'


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = TagCreateForm


class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = ArticleCreateForm


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article_list')


class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')