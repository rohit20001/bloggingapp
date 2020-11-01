from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator

from main.models import Post
from main.forms import Contactform


# Create your views here.
def index(request):
   return render(request, 'main/index.html')    

def blog(request):
    posts = Post.objects.all().order_by('-posted_date')
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
    return render(request, 'main/blog.html', context)

def post(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'main/post.html', context)

def contact(request):
    form =Contactform(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('contact')
    context={'form':form}
    return render(request, 'main/contact.html',context)