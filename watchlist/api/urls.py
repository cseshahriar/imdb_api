from django.urls import path
from watchlist.api.views import (
    StreamPlatformListAPIView, StreamPlatformDetailAPIView,
    watch_list, watch_list_details,
    WatchListAPIView, WatchListDetalAPIView
)

urlpatterns = [

    # fbv
    path('v1/watchlist/', watch_list),
    path('v1/watchlist/<int:pk>/', watch_list_details),
    
    # stream platform
    path('v2/stream/', StreamPlatformListAPIView.as_view(), name='stream-list'),
    path('v2/stream/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='stream-detail'),

    # APIView
    path('v2/watchlist/', WatchListAPIView.as_view(), name='watch-list'),
    path('v2/watchlist/<int:pk>/', WatchListDetalAPIView.as_view(), name='watch-detail'),
]