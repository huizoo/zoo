from rest_framework import serializers
from ..models import Actor, Movie

# 전체 영화배우 목록
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 단일배우 정보제공 (출연한 영화 제목포함)
class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'