from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    pass

@api_view(['GET'])
def actor_detail(request, actor_pk):
    pass

@api_view(['GET'])
def movie_list(request, movie_pk):
    pass

@api_view(['GET'])
def movie_detail(request, movie_pk):
    pass

@api_view(['POST'])
def create_review(request, movie_pk):
    pass

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    pass

