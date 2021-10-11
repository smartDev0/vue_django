from rest_framework import serializers
from vue_app.models import Tweets


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tweets 
        fields=('TweetId','Name','Description','DateOfJoining')