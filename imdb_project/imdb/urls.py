from django.urls import path, include
from rest_framework.routers import DefaultRouter

from imdb.views import MoviewView
# from .views import MovieViewSet

# router = DefaultRouter()
# router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('imdb_movie/', MoviewView.as_view()),
]