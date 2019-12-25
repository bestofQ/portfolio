from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

# Create your views here.

def blog_Page(request):
	blogs = Blog.objects
	return render(request, 'blog.html', {'blogs': blogs})

def blog_text(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'text.html', {'blog': blog})