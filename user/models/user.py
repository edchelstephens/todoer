from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """The app AUTH_USER_MODEL."""
    
    name = models.CharField(max_length=150)
    facebook_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    friends = models.ManyToManyField("self", through="Friendship")
  
    class Meta:
        app_label = "user"    
        db_table = "users"


class Friendship(models.Model):
    """Friendship intermediate model for users."""

    inviter = models.ForeignKey(
        "User", 
        on_delete=models.CASCADE, 
        related_name="friendships_invites"
    )
    invitee = models.ForeignKey(
        "User", 
        on_delete=models.CASCADE,
        related_name="friendships_invited"
    )
    is_accepted = models.BooleanField(default=False)
    datetime_invited = models.DateTimeField(auto_now_add=True)
    datetime_accepted = models.DateTimeField()


    class Meta:
        app_label = "user"
        db_table = "friendships"