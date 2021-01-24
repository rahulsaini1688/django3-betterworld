from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog

def blog_home(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/blog_home.html', {'Blogs': blogs})

def blog_detail(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	return render(request, 'blogs/blog_detail.html', {'Blog': blog})
