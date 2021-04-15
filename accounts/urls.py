# ./bookstore_app/api/urls.py

from django.urls import include, path
from root.api.v1 import accounts

urlpatterns = [
    path('me', accounts.me),
]
