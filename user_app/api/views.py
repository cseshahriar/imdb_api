from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

@api_view(['POST'])
def registration(request):
    """ api register views """
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()

            data['response'] = "Registration Successfull!"
            data['username'] = user.username
            data['email'] = user.email
            
            token = Token.objects.get(user=user).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)

@api_view(['POST'])
def logout(request):
    """ api logout views """

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)