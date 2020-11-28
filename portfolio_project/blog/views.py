from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # This alternative syntax will order by latest first and return 5 only
    # blogs = Blog.objects.order_by('-date')[:5]
    blogs = Blog.objects.order_by('-date')
    # blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html',
                {'blogs':blogs, 'length':len(blogs)})

def detail(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
