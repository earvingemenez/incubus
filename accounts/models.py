from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """ Model class for User's additional
        fields
    """
    user = models.OneToOneField(User)

    def __str__(self):
        return "{}".format(self.user.username)