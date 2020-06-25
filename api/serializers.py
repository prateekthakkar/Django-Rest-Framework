from rest_framework import serializers
from .models import *

# #  Django REST Framework  Serializer 
# class articalSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     author = serializers.CharField(max_length=50)
#     email = serializers.EmailField(max_length=254)
#     date = serializers.DateTimeField()

#     def create(self,validated_data):
#         return Article.objects.create(validated_data)

#     def create(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.author = validated_data.get('author',instance.author)
#         instance.email = validated_data.get('email',instance.email)
#         instance.date = validated_data.get('date',instance.date)
#         instance.save()
#         return instance

#  REST Framework Modal Serializer
class articalSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Article
        # fields = ['id', 'title', 'author']
        fields = '__all__'
