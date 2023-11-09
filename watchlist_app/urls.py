from django.urls import path
from . import views

urlpatterns = [
    path('list/', view=views.movie_list, name='movie-list'),
    path('list/<int:id>/', view=views.movie_detail, name='movie-detail'),
]
