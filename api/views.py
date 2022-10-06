from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializer import UserSerilaizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
# Create your views here.
class UserView(APIView):
    permission_classes = [IsAdminUser]

    print('ddddddddddddd')
    def get(self,format=None):
        print('get method')
        users=User.objects.all()
        serilazer=UserSerilaizer(users,many=True)
        return Response(serilazer.data)
    def post(self,request):
        serila=UserSerilaizer(data=request.data)
        if serila.is_valid(raise_exception=True):
            serila.create(validated_data=request.data)
            return Response(serila.data,status=status.HTTP_201_CREATED)    
        return Response({'error':True,"error_msg":serila.error_messages},status=status.HTTP_400_BAD_REQUEST)    