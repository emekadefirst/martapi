from api.dependencies import *

class ProductViewSet(APIView):
    """
    Allows users to fetch available products in the database
    
    """
    
    def get(self, request):
        query = Product.objects.all()
        serializer_class = ProductSerializer(query, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
