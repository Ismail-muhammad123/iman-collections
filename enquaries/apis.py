from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import EnquirySerializer
from rest_framework.response import Response


class EnquiryList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        enquiries = request.user.enquiries.all()

        serializer = EnquirySerializer(instance=enquiries, many=True)
        return Response(serializer.data)


class EnquiryDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        seriializer = EnquirySerializer(data=request.data)
        if seriializer.is_valid():
            seriializer.save(user=request.user)
            return Response(seriializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seriializer.errors, status=status.HTTP_400_BAD_REQUEST)
