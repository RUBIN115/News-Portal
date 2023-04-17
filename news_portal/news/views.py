from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import NewsFilter
from .forms import NewForm

class NewsList(ListView):
    # model = Post
    queryset = Post.objects.filter(type=0)
    ordering = '-date_time_create'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    form_class = NewForm


class SearchNewsList(ListView):
    queryset = Post.objects.filter(type=0)
    ordering = '-date_time_create'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class AddNew(CreateView):
    template_name = 'new_add.html'
    form_class = NewForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.objects.filter(type=0)
        return super().form_valid(form)


class UpdateNew(UpdateView):
    template_name = 'new_update.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
class DeleteNew(DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'new'