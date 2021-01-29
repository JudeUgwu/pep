from django.shortcuts import render ,  get_object_or_404
from .models import BlogModel

# Create your views here.
def blog(request):
  posts = BlogModel.objects.order_by("date")[:2]
  return render(request,"blog/blog.html",{"posts":posts}) 

def detail(request,blog_id):
  blog = get_object_or_404(BlogModel,pk=blog_id)
  return render(request,"blog/detail.html",{"blog":blog})
