# Library API + JWT

REST API для бібліотеки з JWT-аутентифікацією.
Зроблено на Django + DRF + SimpleJWT.
GitHub: https://github.com/ohnista-lks07/BooksDRF

## Технології
- Python 3.x
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt

## Встановлення та запуск

### 1. Клонуй репозиторій
```bash
git clone https://github.com/ohnista-lks07/BooksDRF.git
cd BooksDRF
```

### 2. Створи віртуальне середовище
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Встанови залежності
```bash
pip install -r requirements.txt
```

### 4. Застосуй міграції
```bash
python manage.py migrate
```

### 5. Створи адміністратора
```bash
python manage.py createsuperuser
```

### 6. Запусти сервер
```bash
python manage.py runserver
```

Проект буде доступний на http://127.0.0.1:8000/

## Auth Endpoints

| Метод | URL | Опис |
|-------|-----|------|
| POST | /api/register/ | Реєстрація нового користувача |
| POST | /api/token/ | Логін — отримати access + refresh |
| POST | /api/token/refresh/ | Оновити access токен |

## CRUD Endpoints

| Метод | URL | Авторизація | Опис |
|-------|-----|-------------|------|
| GET | /api/authors/ | Немає | Список авторів |
| POST | /api/authors/ | Bearer Token | Додати автора |
| GET | /api/authors/{id}/ | Немає | Деталі автора |
| PUT | /api/authors/{id}/ | Bearer Token | Оновити автора |
| DELETE | /api/authors/{id}/ | Bearer Token | Видалити автора |
| GET | /api/books/ | Немає | Список книг з автором |
| POST | /api/books/ | Bearer Token | Додати книгу |
| GET | /api/books/{id}/ | Немає | Деталі книги |
| PUT | /api/books/{id}/ | Bearer Token | Оновити книгу |
| DELETE | /api/books/{id}/ | Bearer Token | Видалити книгу |

## Авторизація

GET запити — публічні, доступні без токена.
Решта (POST, PUT, PATCH, DELETE) — потребують JWT токена у заголовку:
`Authorization: Bearer <access_token>`
main

## Запуск через Docker

1. `git clone ...`
2. `cp .env.example .env`
3. `docker-compose up --build`
4. `docker-compose exec web python manage.py migrate`
5. `docker-compose exec web python manage.py createsuperuser`
6. Відкрий http://localhost:8000/admin