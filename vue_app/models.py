from django.db import models

# Create your models here.

class Tweets(models.Model):
    TweetId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    DateOfJoining = models.DateTimeField(auto_now_add=True)

