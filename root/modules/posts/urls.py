# ./bookstore_app/api/urls.py

from django.urls import include, path
from root.api.v1 import posts

urlpatterns = [
    path('all', posts.get_all_posts),
    path('get', posts.get_posts_by_user),
    path('get/<int:post_id>', posts.get_post),
    path('create', posts.create_post),
    path('update/<int:post_id>', posts.update_post),
    path('delete/<int:post_id>', posts.delete_post),
]
