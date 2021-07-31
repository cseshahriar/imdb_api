from rest_framework.throttling import UserRateThrottle


class RevewCreaeThrottle(UserRateThrottle):
    scope = 'review-create'


class RevewListThrottle(UserRateThrottle):
    scope = 'review-list'