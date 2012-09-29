from django.views.generic import DetailView, ListView
from blog.models import Postagem

class BlogView(ListView):
    model = Postagem


class BlogPostView(DetailView):
    model = Postagem
    context_object_name = 'postagem'
    paginate_by = 3
    