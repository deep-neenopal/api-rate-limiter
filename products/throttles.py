from rest_framework.throttling import UserRateThrottle


class PostProductThrottle(UserRateThrottle):
    scope = 'add_product'

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        if request.method == 'POST':
            return True
        return super().allow_request(request, view)

    def wait(self):
        # Return the wait time if the rate limit has been exceeded
        return super().wait()


class GetProductThrottle(UserRateThrottle):
    scope = 'list_products'

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        if request.method == 'GET':
            return True
        return super().allow_request(request, view)

    def wait(self):
        # Return the wait time if the rate limit has been exceeded
        return super().wait()


class ProductDetailThrottle(UserRateThrottle):
    scope = 'retrieve_product'

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        return super().allow_request(request, view)

    def wait(self):
        # Return the wait time if the rate limit has been exceeded
        return super().wait()
