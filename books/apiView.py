from django.contrib.auth.models import User
from books.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'image', 'totalPages', 'pagesRead', 'timeTaken', 'status']
        read_only_fields = ['user']
    
    # automatically assign the user to the transaction
    def validate(self, attrs):
        # user = User.objects.filter(username=self.context['request'].user)[0]
        attrs['user'] = self.context['request'].user
        return attrs

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'created_at']
        read_only_fields = ['user', 'book']

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
        return Book.objects.filter(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# get logged in user's details
class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
