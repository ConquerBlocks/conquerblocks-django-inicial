
from books.models import Editorial
from django.http import Http404
from django.core.exceptions import PermissionDenied

def user_can_delete_editorial(function):
    def wrap(request, *args, **kwargs):
        try:
            editorial = Editorial.objects.get(pk=kwargs["pk"])
        except Editorial.DoesNotExist:
            raise Http404

        if request.user == editorial.created_by:
            return function(request, *args, **kwargs)

        raise PermissionDenied

    return wrap