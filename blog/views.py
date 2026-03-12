from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'