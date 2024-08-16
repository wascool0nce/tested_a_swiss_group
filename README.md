# tested_a_swiss_group
Разработать веб сервис для работы с учетными записями пользователей со следующей функциональностью:
    1. Создание пользователя
    2. Получение пользователя по id
    3. Поиск пользователя по одному или нескольким полям: фамилия, имя, отчество, телефон, email.
Атрибуты пользователя:
    • Id
    • фамилия
    • имя
    • отчество
    • дата рождения
    • номер паспорта (вместе с серией в формате ХХХХ ХХХХХХ)
    • место рождения
    • телефон (в формате 7ХХХХХХХХХХ)
    • емейл
    • адрес регистрации
    • адрес проживания
Пользователь может быть создан из разных приложений. В зависимости от приложения отличается логика валидации полей при создании учетной записи пользователя. Приложение определяется по обязательному для указания http-заголовку "x-Device".
Список значений http-заголовка и правила валидации полей:
    • mail - только имя и емейл обязательные
    • mobile - только номер телефона обязательный
    • web - все поля кроме емейла и адреса проживания обязательные
Стек: django, drf
Дополнительные требования: 
    • основная бизнес-логика должна быть покрыта интеграционными тестами
    • в проекте должен быть docker-compose для подготовки окружения для локального запуска сервиса
    • исходники проекта выложить на github
Срок выполнения неделя.