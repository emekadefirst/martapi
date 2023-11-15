from api.dependencies import *
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterUserView(APIView):
    def post(self, request):
        data = request.data  # Assuming you send a JSON request with the provided data

        # Use the BuyerSerializer for registration
        serializer = BuyerSerializer(data=data)

        if serializer.is_valid():
            # Create a User instance
            user = User.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                password=data['password'],
                email=data['email']
            )

            # Create the Buyer instance associated with the user
            buyer = Buyer(
                user=user,
                phone_number=data['phone_number'],
                street_address=data['street_address'],
                land_mark=data['land_mark'],
                LGA=data['LGA'],
                state=data['state']
            )
            buyer.save()

            # Create a token for the user
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key, 'user': BuyerSerializer(buyer).data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)  # Use the UserSerializer

        return Response({'success': True, 'token': token.key, 'user': serializer.data})



class BuyerDetailView(APIView):
    def get_object(self, user_id):
        try:
            return Buyer.objects.get(user_id=user_id)
        except Buyer.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        buyer = self.get_object(user_id)
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        buyer = self.get_object(user_id)
        serializer = BuyerSerializer(buyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        buyer = self.get_object(user_id)
        buyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
