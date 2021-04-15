from abc import ABC, abstractmethod

# Abstract Class for interface


class PostDbAccessor(ABC):

    @abstractmethod
    def get_all_posts(self):
        pass

    @abstractmethod
    def get_posts_by_user(self, user):
        pass

    @abstractmethod
    def get_post_by_id(self, post_id):
        pass

    @abstractmethod
    def create_post(self, post):
        pass

    @abstractmethod
    def update_post(self, post):
        pass

    @abstractmethod
    def delete_post(self, post_id):
        pass
