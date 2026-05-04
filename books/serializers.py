from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # Покажемо ім'я автора текстом — зручніше для читання
    author_name = serializers.CharField(
        source='author.name',
        read_only=True,
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'year', 'isbn']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
