from django.urls import path
from .views import (home_view, about_view, contact_view, blog_detail_view, category_view,
                    search_view,tag_posts_view)

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('blog/<int:pk>/', blog_detail_view),
    path('categories/', category_view),
    path('search/', search_view),
    path('tag/<int:pk>/', tag_posts_view),
]
