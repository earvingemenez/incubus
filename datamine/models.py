from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models


class DataMine(models.Model):
    """ Model class that contains information of
        the client's data mining request
    """
    NORMAL = 'normal'
    SCHEDULED = 'scheduled'
    MINE_TYPE = (
        (NORMAL, 'One Time Scraping'),
        (SCHEDULED, 'Scheduled Scraping'),
    )

    PENDING = 'pending'
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    STATUSES = (
        (PENDING, 'Pending'),
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )

    user = models.ForeignKey(User)

    title = models.CharField(max_length=200)
    mine_type = models.CharField(max_length=50, choices=MINE_TYPE, default=NORMAL)
    sites = models.ManyToManyField('DataMineUrl', blank=True)
    notes = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUSES, default=PENDING)
    date_created = models.DateTimeField(auto_now_add=True)

    data_model = models.ForeignKey(ContentType, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)


class DataMineUrl(models.Model):
    """ Model class that will contain URLS that will be
        scraped by the spiders
    """
    url = models.URLField()

    def __str__(self):
        return "{}".format(self.url)