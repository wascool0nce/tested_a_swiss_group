from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer, UserCreateMailSerializer, UserCreateMobileSerializer, \
    UserCreateWebSerializer
from .swagger_schema import RESPONSE_GET_USER, RESPONSE_CREATE_USER, ID_PARAMETER, DEVICE_HEADER


class UserViewSet(GenericViewSet):
    @swagger_auto_schema(**ID_PARAMETER, method='GET', responses=RESPONSE_GET_USER, tags=["user"])
    @action(detail=False, methods=['GET'])
    def retrieve_user(self, request, pk=None):
        """Получение пользователя по ID"""
        try:
            id = request.query_params.get('id')
            user = User.objects.get(pk=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(manual_parameters=[DEVICE_HEADER], method='POST', request_body=UserSerializer,
                         responses=RESPONSE_CREATE_USER, tags=["user"])
    @action(detail=False, methods=['POST'])
    def create_user(self, request):
        """Создание нового пользователя"""
        device_type = request.headers.get('x-Device')

        # Выбор сериализатора в зависимости от типа устройства
        if device_type == 'mail':
            serializer = UserCreateMailSerializer(data=request.data)
        elif device_type == 'mobile':
            serializer = UserCreateMobileSerializer(data=request.data)
        elif device_type == 'web':
            serializer = UserCreateWebSerializer(data=request.data)
        else:
            return Response({"error": "Недопустимый тип устройства."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
