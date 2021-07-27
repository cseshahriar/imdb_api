from django.urls import path
from watchlist.api.views import (
    StreamPlatformListAPIView, StreamPlatformDetailAPIView,
    watch_list, watch_list_details,
    WatchListAPIView, WatchListDetalAPIView,
    ReviewListCreateGenericsAPIView,
    ReviewDetailGenericsAPIView,
    ReviewListGenerics, ReviewDetailGenerics, ReviewCreateGenerics
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

    # generics mixins
    path('v3/stream/<int:pk>/reviews/', ReviewListCreateGenericsAPIView.as_view(), name='review-list'),
    path('v3/stream/reviews/<int:pk>', ReviewDetailGenericsAPIView.as_view(), name='review-detail'),

    # generics
    path('v4/stream/<int:pk>/reviews/', ReviewListGenerics.as_view(), name='v4-review-list'),
    path('v4/stream/<int:pk>/reviews-create/', ReviewCreateGenerics.as_view(), name='v4-review-creae'),
    path('v4/stream/reviews/<int:pk>', ReviewDetailGenerics.as_view(), name='v4-review-detail'),

]