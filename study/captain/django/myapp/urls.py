from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('samsung01/', views.index, name='index'),
]
