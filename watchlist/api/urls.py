from django.urls import path
from watchlist.api.views import movie_list, movie_details

urlpatterns = [
    path('list/', movie_list),
    path('<int:pk>/detail/', movie_details),
]