from rest_framework import serializers
from .models import ArtiLes, Comment, Category

class ArtiLesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtiLes
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'