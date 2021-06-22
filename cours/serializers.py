from rest_framework import serializers
from .models import Cours ,CoursImage ,Category


class ImageCoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursImage
        fields = "__all__"


class CoursSerializer(serializers.ModelSerializer):
    images = ImageCoursSerializer(many=True, read_only=True)
    class Meta:
        model = Cours
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    categorys = CoursSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
