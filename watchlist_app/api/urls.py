from django.urls import path
from . import views

urlpatterns = [
    path('list/', view=views.DigitalContentListAV.as_view(), name='movie-list'),
    path('list/<int:id>/', view=views.DigitalContentDetailAV.as_view(), name='movie-detail'),
    path('platform/', views.StreamingPlatformList.as_view(), name='platform-list'),
    path('platform/<int:id>/', views.StreamingPlatformDetail.as_view(), name='platform-detail'),
]