from django.db import models
from django.contrib.auth.models import AbstractUser
 
class CustomUser(AbstractUser):
    model = AbstractUser
    follows = models.ManyToManyField(
        'CustomUser',
        verbose_name='フォロー',
        through='FollowerShip',
        through_fields=('follower', 'followee'),
        related_name='+'
    )
    followers = models.ManyToManyField(
        'CustomUser',
        verbose_name='フォロワー',
        through='FollowerShip', 
        through_fields=('followee', 'follower'),
        related_name='+'
    )
    def follows_ids(self):
        return [following_user.id for following_user in self.follows.all()]
 
class Followership(models.Model):
    model = AbstractUser
    follower = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='followee_followerships')
    followee = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='follower_followerships')
 
    class Meta:
        # follower と followee の組み合わせはユニーク
        unique_together = ('follower', 'followee')
        
        