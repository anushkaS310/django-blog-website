
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from .models import Post
# Create your views here.
# posts= [
#     {
#         "slug":"sacac",
#         "image":"xc",
#         "author":"sara",
#         "date": date(2021,10,3),
#         "title":"Scene",
#         "tag":"sdcsc",
#         "content":"casdxax"
#     },
#     {
#         "slug":"sacac",
#         "image":"xc",
#         "author":"sara",
#         "date": date(2021,10,3),
#         "title":"Scene",
#         "tag":"sdcsc",
#         "content":"casdxax"
#     },
#     {
#         "slug":"sacac",
#         "image":"xc",
#         "author":"sara",
#         "date": date(2021,10,3),
#         "title":"Scene",
#         "tag":"sdcsc",
#         "content":"casdxax"
#     },
#     {
#         "slug":"sacac",
#         "image":"xc",
#         "author":"sara",
#         "date": date(2021,10,3),
#         "title":"Scene",
#         "tag":"sdcsc",
#         "content":"casdxax"
#     },
#     {
#         "slug":"sacac",
#         "image":"xc",
#         "author":"sara",
#         "date": date(2021,10,3),
#         "title":"Scene",
#         "tag":"sdcsc",
#         "content":"casdxax"
#     },
# ]


def home_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    # sorted_posts=sorted(posts, key=get_date)
    # latest_posts=sorted_posts[-3:]
    return render(request,"blog/home_page.html" ,{
        "posts":latest_posts,
    })

def all_posts(request):
    posts=Post.objects.all()
    return render(request,"blog/all_posts.html" ,{
        "posts":posts,
    });

def post_details(request ,slug):
    identified_post=get_object_or_404(Post,slug=slug)
    return render(request, "blog/post_details.html",{
        "p":identified_post,

    })