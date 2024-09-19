from django.core.cache import caches
from rest_framework.throttling import UserRateThrottle, SimpleRateThrottle


class PostProductThrottle(UserRateThrottle):
    scope = 'add_product'

    # Override the get_cache_key method to use a different identifier
    def get_cache_key(self, request, view):
        # Create a session for anonymous users
        if not request.session.session_key:
            request.session.create()  # This forces the session to be created

        # Now the session_key should be available
        print(f"Session Key: {request.session.session_key}")
        return f'throttle_{request.session.session_key}'

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        if request.method == 'POST':
            return super().allow_request(request, view)
        return True

    def wait(self):
        # Return the wait time if the rate limit has been exceeded
        return super().wait()


class GetProductThrottle(SimpleRateThrottle):
    scope = 'list_products'
    cache = caches['alternate']

    # Override the get_cache_key method to use a different identifier
    def get_cache_key(self, request, view):
        # Create a session for anonymous users
        if not request.session.session_key:
            request.session.create()  # This forces the session to be created

        # Now the session_key should be available
        return f'throttle_{self.scope}_{request.session.session_key}'

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        if request.method == 'GET':
            return super().allow_request(request, view)
        return True

    def wait(self):
        # Return the wait time if the rate limit has been exceeded
        return super().wait()


class ProductDetailThrottle(UserRateThrottle):
    scope = 'retrieve_product'
    cache = caches['alternate']

    # Override the get_cache_key method to use a different identifier
    def get_cache_key(self, request, view):
        # Create a session for anonymous users
        if not request.session.session_key:
            request.session.create()  # This forces the session to be created

        # Now the session_key should be available
        return f'throttle_{self.scope}_{request.session.session_key}'

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        return super().allow_request(request, view)

    def wait(self):
        # Return the wait time if the rate limit has been exceeded
        return super().wait()
