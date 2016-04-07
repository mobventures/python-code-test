from django.db import models
from django.contrib.auth.models import User
from items.models import PhotoItem, TweetItem

class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    photo_item = models.ForeignKey(PhotoItem, blank=True, null=True)
    tweet_item = models.ForeignKey(TweetItem, blank=True, null=True)
