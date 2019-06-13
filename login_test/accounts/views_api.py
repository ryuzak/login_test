from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import UserSerializer
from .models import User

class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetreiveUsersAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetreiveUpdateUserAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):
		serializer = UserSerializer(request.user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		serializer_data = request.data.get('user',{})
		serializer = UserSerializer(request.user, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, *args, **kwargs):
		serializer_data = request.data.get('user',{})
		serializer_data['is_active'] = False
		serializer = UserSerializer(request.user, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)