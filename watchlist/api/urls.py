from django.urls import path
from watchlist.api.views import (
    watch_list, watch_list_details,
    WatchListAPIView, WatchListDetalAPIView
)

urlpatterns = [
    # fbv
    path('v1/watchlist/', watch_list),
    path('v1/watchlist/<int:pk>/', watch_list_details),

    # APIView
    path('v2/watchlist/', WatchListAPIView.as_view()),
    path('v2/watchlist/<int:pk>/', WatchListDetalAPIView.as_view()),
]