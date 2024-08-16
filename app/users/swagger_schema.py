from drf_yasg import openapi

ID_PARAMETER = {
    'manual_parameters': [
        openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True,
                          description='Id пользователя'),
    ],
}

DEVICE_HEADER = openapi.Parameter(
    'x-Device',
    in_=openapi.IN_HEADER,
    description='Тип устройства, определяющий логику валидации (mail, mobile, web)',
    type=openapi.TYPE_STRING,
    required=True
)

RESPONSE_CREATE_USER = {
    '200': openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пользователя'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Фамилия'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя'),
                'middle_name': openapi.Schema(type=openapi.TYPE_STRING, description='Отчество'),
                'date_of_birth': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата рождения'),
                'passport_number': openapi.Schema(type=openapi.TYPE_STRING, description='Номер паспорта'),
                'place_of_birth': openapi.Schema(type=openapi.TYPE_STRING, description='Место рождения'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Телефон'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Электронная почта'),
                'registration_address': openapi.Schema(type=openapi.TYPE_STRING, description='Адрес регистрации'),
                'residential_address': openapi.Schema(type=openapi.TYPE_STRING, description='Адрес проживания')
            }
        )
    ),
    '400': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=[
                    'invalid_data',  # Например, когда данные не прошли валидацию
                    'user_not_found',  # Например, если пользователь с указанным ID не найден
                ],
                description='Описание ошибки'
            )
        }
    )
}

RESPONSE_GET_USER = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пользователя'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Фамилия'),
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя'),
            'middle_name': openapi.Schema(type=openapi.TYPE_STRING, description='Отчество', nullable=True),
            'date_of_birth': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата рождения'),
            'passport_number': openapi.Schema(type=openapi.TYPE_STRING, description='Номер паспорта'),
            'place_of_birth': openapi.Schema(type=openapi.TYPE_STRING, description='Место рождения'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Телефон'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Электронная почта'),
            'registration_address': openapi.Schema(type=openapi.TYPE_STRING, description='Адрес регистрации'),
            'residential_address': openapi.Schema(type=openapi.TYPE_STRING, description='Адрес проживания')
        }
    ),
    '400': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=[
                    'invalid_id',  # Если передан некорректный ID
                ]
            )
        }
    ),
    '404': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='Пользователь не найден'
            )
        }
    )
}


