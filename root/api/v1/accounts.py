from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse

from accounts.models import UserAccount
from accounts.serializers import UserSerializer
import accounts.utils as utils


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    user_id = utils.get_user_id_by_request(request)
    user = UserAccount.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )
