from rest_framework.throttling import UserRateThrottle


class ProductThrottle(UserRateThrottle):
    scope = 'list_products'
    def get_scope(self, request):
        # Verify the request method and set a different scope
        if request.method == "GET":
            return 'list_products'  # Scope for GET requests
        elif request.method == "POST":
            return 'add_product'  # Scope for POST requests
        return self.scope

    def allow_request(self, request, view):
        # Call the parent method to check the rate limit
        self.scope = self.get_scope(request)
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
