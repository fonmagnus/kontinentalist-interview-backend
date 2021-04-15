from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from django.shortcuts import render

from root.modules.posts.models import Post
from root.modules.posts.serializers import PostSerializer
from root.modules.posts.permissions import IsPostOwner, IsAdminUser
from root.services import post_service
from accounts.models import UserAccount
import accounts.utils as utils

import ipdb
import jwt
import json
import logging


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_all_posts(request):
    posts = post_service.get_all_posts()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_posts_by_user(request):
    user_id = utils.get_user_id_by_request(request)
    posts = post_service.get_posts_by_user(UserAccount.objects.get(id=user_id))
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPostOwner])
def get_post(request, post_id):
    post = post_service.get_post_by_id(post_id)
    serializer = PostSerializer(post, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request):
    title = request.data.get('title')
    content = request.data.get('content')
    user_id = utils.get_user_id_by_request(request)
    post_obj = Post(title=title, content=content,
                    posted_by=UserAccount.objects.get(id=user_id))
    try:
        result = post_service.create_post(post_obj)
        serializer = PostSerializer(result, many=False)
        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=200
        )
    except Exception as e:
        logging.exception("message")
        return JsonResponse(
            data={
                "message": "Unexpected server error"
            },
            status=500
        )


@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsPostOwner])
def update_post(request, post_id):
    payload = json.loads(request.body)
    try:
        result = post_service.update_post(post_id, payload)
        serializer = PostSerializer(result, many=False)
        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=200
        )
    except Exception as e:
        logging.exception("message")
        return JsonResponse(
            data={
                "message": "Unexpected Server Error"
            },
            status=500
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsPostOwner])
def delete_post(request, post_id):
    post_service.delete_post(post_id)
    return JsonResponse(
        data={
            "message": "Successfully delete post"
        },
        status=200
    )
