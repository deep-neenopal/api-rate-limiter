from rest_framework.throttling import UserRateThrottle


class ProductThrottle(UserRateThrottle):
    rate = '1000/day'


class ProductDetailThrottle(UserRateThrottle):
    rate = '3/minute'
