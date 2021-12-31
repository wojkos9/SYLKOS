import random
import string
from users.models import BasicUser

from django.http.request import HttpRequest

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(str(random.choice(chars)) for x in range(length))


def not_authenticated_return(default):
    def decorator(func):
        def decorated(self, *args, **kwargs):
            request: HttpRequest = self.context.get("request")
            if request and request.user.is_authenticated:
                return func(self, *args, **kwargs)
            return default
        return decorated
    return decorator

def get_default_author():
    return BasicUser.objects.filter(is_superuser=True).first().id
