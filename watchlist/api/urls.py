from django.urls import path
from watchlist.api.views import (
    movie_list, movie_details,
    MovieListAPIView, MovieDetalAPIView
)

urlpatterns = [
    # fbv
    path('v1/movies/', movie_list),
    path('v1/movies/<int:pk>/', movie_details),

    # APIView
    path('v2/movies/', MovieListAPIView.as_view()),
    path('v2/movies/<int:pk>/', MovieDetalAPIView.as_view()),
]