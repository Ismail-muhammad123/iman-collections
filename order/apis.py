from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from products.models import Product
from order.models import Order
from .serializers import OrderSerializer
import string
import random
import datetime


characters = string.ascii_lowercase+string.digits


def generate_tracking_id():
    return "".join([characters[random.randint(0, len(characters)-1)] for i in range(6)]).upper()


class OrderList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        oders = request.user.orders.all()
        serializer = OrderSerializer(instance=oders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):

        try:
            order = request.user.orders.get(pk=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(instance=order)
        return Response(serializer.data)


class CreateOrderAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        tracking_id = generate_tracking_id()
        data = request.data
        for i in data:

            price = Product.objects.get(id=i['product']).price
            delivery_days = Product.objects.get(id=i['product']).delivery_days
            total_amount = price * i['quantity']
            i['total_amount'] = total_amount
            i['delivery_date'] = datetime.date.today(
            ) + datetime.timedelta(delivery_days)
            i['tracking_id'] = tracking_id
        serializer = OrderSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
