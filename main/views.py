from django.shortcuts import render

from main.models import Post


# Create your views here.
def index(request):
   return render(request, 'main/index.html')    

def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'main/blog.html', context)