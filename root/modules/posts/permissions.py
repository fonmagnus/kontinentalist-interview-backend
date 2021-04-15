from rest_framework.permissions import BasePermission
import accounts.utils as utils
from .models import UserAccount

from root.modules.posts.models import Post


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        user_id = utils.get_user_id_by_request(request)
        user = UserAccount.objects.get(id=user_id)
        return user.role == 'Admin'


class IsPostOwner(BasePermission):
    def has_permission(self, request, view):
        user_id = utils.get_user_id_by_request(request)
        post_id = view.kwargs.get('post_id')
        return Post.objects.get(id=post_id).posted_by.id == user_id or user.role == 'Admin'
