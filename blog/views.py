from unicodedata import category
from django.shortcuts import render
import blog
from blog.models import Blogs, Category

# Create your views here.
def index(request):
    cat = Category.objects.all()
    context = {'cat': cat}
    return render(request,'blog/index.html', context)

def ReadCat(request, id):
    cats = Category.objects.get(cat_id = id)
    blogs = Blogs.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'blog/read_cat.html', context)


def ReadBlog(request, id):
    blog = Blogs.objects.get(id = id)
    context = {'blog':blog}
    return render(request,'blog/read_blog.html', context)


      