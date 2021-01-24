from django.contrib import admin
from django.urls import path

from Portfolio import views as portfolio_views
from blogs import views as blogs_views

app_name = 'blogs'

urlpatterns = [
    
    path('', blogs_views.blog_home, name = 'all_blogs'),
    path('<int:blog_id>/', blogs_views.blog_detail, name = 'blog_detail')

]