from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm # new
from django.urls import reverse_lazy # new


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    
class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')