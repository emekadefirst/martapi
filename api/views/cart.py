from api.dependencies import *


class CartView(APIView):
    permission_classes = ([SessionAuthentication, TokenAuthentication, IsAuthenticated])
    def get(self, request):
        # Get all items in the cart for the authenticated user
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = Cart(data=data)

        if serializer.is_valid():
            # Set the user to the authenticated user
            serializer.validated_data['user'] = request.user
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, item_id):
        try:
            # Get the cart item by ID
            cart_item = Cart.objects.get(id=item_id, user=request.user)
        except Cart.DoesNotExist:
            return Response({'error': 'CartItem not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = CartSerializer(instance=cart_item, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        try:
            # Get the cart item by ID
            cart_item = Cart.objects.get(id=item_id, user=request.user)
        except Cart.DoesNotExist:
            return Response({'error': 'CartItem not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
