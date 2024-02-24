.. toctree::
   :maxdepth: 1
   :hidden:

   API reference <code>

Портфолио
=========

Сервис для получения актуальной информации о странах и городах.

Зависимости
===========

1. Фреймворк
Django>=4.0.7,<4.1.0
djangorestframework>=3.14.0,<3.15.0

2. Генерация Swagger
drf-yasg>=1.21.4,<1.22.0

3. Работа с переменными окружения
django-environ>=0.9.0,<0.10.0

4. Отладчик для Django
django-debug-toolbar>=3.6.0,<3.7.0

5. Адаптер для подключения к PostgreSQL
psycopg2-binary>=2.9.3,<2.10.0

6. Документация
Sphinx>=5.1.1,<5.2.0
sphinx-rtd-theme>=1.0.0,<2.0.0

7. Статический анализ кода (линтеры)
isort>=5.10.1,<5.11.0
flake8-django>=1.1.5,<1.2.0
pylint-django>=2.5.3,<2.6.0
django-stubs[compatible-mypy]>=1.12.0,<1.13.0

8. Автоматическое форматирование кода
black>=22.8.0,<22.9.0

9. Redis
redis>=4.3.4,<4.4.0

10. Распределенная очередь задач
celery>=5.2.7,<5.3.0
django-celery-beat>=2.3.0,<2.4.0

11. Работа с RabbitMQ
pika>=1.3.1,<1.4.0

12. Работа с HTTP-запросами
httpx>=0.23.0,<0.24.0

13. DTO и валидация данных
pydantic>=1.10.2,<1.11.0


Установка
=========

Установите требуемое ПО:

1. Docker для контейнеризации – |link_docker|

.. |link_docker| raw:: html

   <a href="https://www.docker.com" target="_blank">Docker Desktop</a>

2. Для работы с системой контроля версий – |link_git|

.. |link_git| raw:: html

   <a href="https://github.com/git-guides/install-git" target="_blank">Git</a>

3. IDE для работы с исходным кодом – |link_pycharm|

.. |link_pycharm| raw:: html

    <a href="https://www.jetbrains.com/ru-ru/pycharm/download" target="_blank">PyCharm</a>

Клонируйте репозиторий проекта в свою рабочую директорию:

    .. code-block:: console
        git clone https://github.com/miamib34ch/HSE-Python-CountriesInformer.git


Использование
=============

1. Чтобы управлять вашим API, вам необходимо добавить суперпользователя. Подключитесь к контейнеру Docker-приложения (если вы находитесь вне контейнера):

    .. code-block:: console
        docker-compose exec app bash


2. Создайте суперпользователя:

    .. code-block:: console
        ./manage.py createsuperuser

3. Перейдите по адресу http://0.0.0.0:8020/admin и управляйте вашей базой данных.


Автоматизация
=============

Проект содержит специальный файл Makefile, который предоставляет ярлыки для выполнения определенного набора команд:

Построить Docker-контейнер:

    .. code-block:: console
        make build

Сгенерировать документацию Sphinx:

    .. code-block:: console
        make docs-html

Автоформатирование исходного кода:

    .. code-block:: console
        make format

Статический анализ (линтеры):

    .. code-block:: console
        make lint

Автотесты:

    .. code-block:: console
        make test

Выполнить автоформатирование, статический анализ и тесты одной командой:

    .. code-block:: console
        make all

Запустите эти команды из директории с исходным кодом, где расположен файл Makefile.

