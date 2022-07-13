from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from cart.serializers import CartSerializer


class CartList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
            Get a list of items in the cart of the currently loged-in user 
        """
        cart_items = request.user.cart_items.all()
        serializer = CartSerializer(instance=cart_items, many=True)

        return Response(serializer.data)


class CartSingle(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
            Insert an item in to the list of cart items for the currently loged-in user
        """
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def pust(self, request):
        """
            Update an in the cart with the provided id in the data 
        """
        pk = request.data['id']
        cart = request.user.cart_items.get(pk=pk, user=request.user)
        serializer = CartSerializer(data=request.data, instance=cart)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
