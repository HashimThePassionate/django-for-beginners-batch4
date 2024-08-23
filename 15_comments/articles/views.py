# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import Article
from .forms import CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.views import View  # new
from django.urls import reverse  # new


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class CommentGet(DetailView):  # new
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):  # new
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleDetailView(LoginRequiredMixin, View):  # new
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleCreateView(LoginRequiredMixin, CreateView):  # new
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
