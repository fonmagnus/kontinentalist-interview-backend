from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
