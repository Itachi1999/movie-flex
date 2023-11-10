from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ['active']
        
    def get_len_title(self, object):
        return len(object.title) 

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#     year = serializers.IntegerField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.year = validated_data.get('year', instance.year)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and description cannot be the same')
    
#     def validate_title(self, value):
#         if Movie.objects.filter(title=value).exists():
#             raise serializers.ValidationError('Title already exists')
#         elif len(value) < 2:
#             raise serializers.ValidationError('Title must be at least 2 characters')
#         elif len(value) > 100:
#             raise serializers.ValidationError('Title must be less than 100 characters')
#         return value
    