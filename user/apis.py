from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import AccountSerializer
from rest_framework.response import Response


class UserDetails(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        serializer = AccountSerializer(instance=request.user)

        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = AccountSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
