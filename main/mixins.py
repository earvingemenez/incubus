from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


class AuthenticationMixin(object):

    def __init__(self, *args, **kwargs):
        return super(AuthenticationMixin, self).__init__(*args, **kwargs)

    def login(self, user):
        try:
            login(self.request, user)
        except Exception as e:
            raise e

    def redirect_to(self, next_=None):
        return reverse('dashboard') if not next_ else next_