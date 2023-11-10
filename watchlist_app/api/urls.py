from django.urls import path
from . import views

urlpatterns = [
    path('list/', view=views.MovieListAV.as_view(), name='movie-list'),
    path('list/<int:id>/', view=views.MovieDetailAV.as_view(), name='movie-detail'),
]