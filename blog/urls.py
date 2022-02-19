from django.urls import path
from . import views
urlpatterns =[
   path('',views.home_page,name="home_page"),
   path("all_posts", views.all_posts ,name="all_posts"),
   path("all_posts/<slug:slug>",views.post_details , name="post_details")
]
