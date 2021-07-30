from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

@api_view(['POST'])
def registration(request):
    """ api register views """
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['POST'])
def logout(request):
    """ api logout views """

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)