from django.contrib.auth.models import User
from books.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReadingBookSerializer(ModelSerializer):
    class Meta:
        model = ReadingBook
        fields = ['book', 'date_started', 'date_finished', 'comments']
        read_only_fields = ['user']
    
    # automatically assign the user to the transaction
    def validate(self, attrs):
        user = User.objects.filter(username=self.context['request'].user)[0]
        attrs['user'] = user
        return attrs

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'date', 'review', 'rating']
        read_only_fields = ['reviewer']
    
    # automatically assign the user to the transaction
    def validate(self, attrs):
        user = User.objects.filter(username=self.context['request'].user)[0]
        attrs['user'] = user
        return attrs

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    # sign up new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        if self.request.user.username:
            return Book.objects.all()
        raise Exception('You must be logged in to view books')

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.request.user.username:
            return Review.objects.all()
        raise Exception('You must be logged in to view reviews')

class ReadingBookViewSet(viewsets.ModelViewSet):
    queryset = ReadingBook.objects.all()
    serializer_class = ReadingBookSerializer
    
    def get_queryset(self):
        return ReadingBook.objects.filter(user=self.request.user)

class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# get logged in user's details
class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
