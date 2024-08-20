from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q, F
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer, UserCreateMailSerializer, UserCreateMobileSerializer, UserCreateWebSerializer
from .swagger_schema import RESPONSE_GET_USER, RESPONSE_CREATE_USER, ID_PARAMETER, DEVICE_HEADER, RESPONSE_SEARCH_USER, \
    SEARCH_USER


class UserViewSet(GenericViewSet):
    """
    ViewSet для управления пользователями.
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        Определение класса сериализатора в зависимости от типа устройства.
        """
        if self.action == 'create_user':
            return self._get_create_serializer()
        return UserSerializer

    def _get_create_serializer(self):
        """
        Выбор сериализатора на основе заголовка `x-Device`.
        """
        device_type = self.request.headers.get('x-Device')
        if device_type == 'mail':
            return UserCreateMailSerializer
        elif device_type == 'mobile':
            return UserCreateMobileSerializer
        elif device_type == 'web':
            return UserCreateWebSerializer
        return UserSerializer

    @swagger_auto_schema(**ID_PARAMETER, method='GET', responses=RESPONSE_GET_USER, tags=["user"])
    @action(detail=False, methods=['GET'], url_path='retrieve')
    def retrieve_user(self, request):
        """
        Получение пользователя по ID.
        """
        user_id = request.query_params.get('id')
        try:
            user = self.get_queryset().get(pk=user_id)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(manual_parameters=[DEVICE_HEADER], method='POST', request_body=UserSerializer,
                         responses=RESPONSE_CREATE_USER, tags=["user"])
    @action(detail=False, methods=['POST'], url_path='create')
    def create_user(self, request):
        """
        Создание нового пользователя.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(method='GET', manual_parameters=[SEARCH_USER], responses=RESPONSE_SEARCH_USER, tags=["user"])
    @action(detail=False, methods=['GET'], url_path='search')
    def search_user(self, request):
        """
        Поиск пользователей по заданному запросу.
        """
        search_query = request.GET.get('search', '')
        if search_query:
            query = SearchQuery(search_query, config='russian')
            users = self.get_queryset().annotate(
                rank=SearchRank(F('search_vector'), query)
            ).filter(search_vector=query).order_by('-rank')
        else:
            users = self.get_queryset().none()

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
