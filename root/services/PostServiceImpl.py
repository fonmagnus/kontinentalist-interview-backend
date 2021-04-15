from .PostService import PostService
from root.repositories.PostDbAccessorImpl import PostDbAccessorImpl


class PostServiceImpl(PostService):

    def __init__(self, *args, **kwargs):
        self.db_accessor = PostDbAccessorImpl()

    def get_all_posts(self):
        return self.db_accessor.get_all_posts()

    def get_posts_by_user(self, user):
        return self.db_accessor.get_posts_by_user(user)

    def get_post_by_id(self, post_id):
        return self.db_accessor.get_post_by_id(post_id)

    def create_post(self, post):
        return self.db_accessor.create_post(post)

    def update_post(self, post_id, payload):
        return self.db_accessor.update_post(post_id, payload)

    def delete_post(self, post_id):
        return self.db_accessor.delete_post(post_id)
