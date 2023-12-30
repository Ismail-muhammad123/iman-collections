from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import StoreSerializer
from rest_framework.response import Response
from .models import Store


class StoreDetails(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        store = request.user.store
        if store is not None:
            serializer = StoreSerializer(instance=store)

            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        files = request.FILES

        store = request.user.store
        if store is not None:
            serializer = StoreSerializer(instance=store, data=data, files=files)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class CreateStoreAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        data = request.data
        files = request.FILES

        store = request.user.store
        if store is None:
            serializer = StoreSerializer(data=data, files=files)
            if serializer.is_valid():
                serializer.create(serializer.validated_data)
                return Response(serializer, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
