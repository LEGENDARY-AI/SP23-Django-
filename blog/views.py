from django.views.generic import ListView  
from .models import Post  

class PostListView(ListView):  
    model = Post  
    template_name = 'blog/post_list.html'  # Create this template
    context_object_name = 'posts'