from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import AccountSerializer
from rest_framework.response import Response


class UserDetails(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        serializer = AccountSerializer(instance=request.user)

        return Response(serializer.data)
