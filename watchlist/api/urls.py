from django.urls import path
from watchlist.api.views import movie_list, movie_details

urlpatterns = [
    path('', movie_list),
    path('<int:pk>/', movie_details),
]