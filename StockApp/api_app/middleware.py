from django.utils.depreciation import MiddlewareMixin
from .models import APICount

class APICountMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if "api" in request.path:
            api_count, created = APICount.objects.get_or_create(id=1)
            api_count.count += 1
            api_count.save()

        return None