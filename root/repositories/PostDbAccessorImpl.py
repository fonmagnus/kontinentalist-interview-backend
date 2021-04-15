from .PostDbAccessor import PostDbAccessor
from django.db.models import Q
from root.modules.posts.models import Post

import ipdb


class PostDbAccessorImpl(PostDbAccessor):

    def get_all_posts(self):
        return Post.objects.all()

    def get_posts_by_user(self, user):
        return Post.objects.filter(Q(posted_by=user))

    def get_post_by_id(self, post_id):
        return Post.objects.get(id=post_id)

    def create_post(self, post):
        return Post.objects.create(
            title=post.title,
            content=post.content,
            posted_by=post.posted_by
        )

    def update_post(self, post_id, payload):
        post_item = Post.objects.filter(id=post_id)
        post_item.update(**payload)
        return Post.objects.get(id=post_id)

    def delete_post(self, post_id):
        post_item = Post.objects.get(id=post_id)
        post_item.delete()
