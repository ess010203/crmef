from django.db.models import fields
from rest_framework import serializers
from .models import News , FileNews



class FileNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileNews
        fields = "__all__"


class NewsSerializers(serializers.ModelSerializer):
    filesNews = FileNewsSerializer(many=True, read_only=True)
    class Meta:
        model = News
        fields = '__all__'

