from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
 
class Photo(models.Model):
    body = models.CharField("本文", max_length=200)
    image = models.ImageField("画像", blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="投稿者")
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    liked_users = models.ManyToManyField(get_user_model(), related_name="likes") # いいねしたユーザー
 
    def __str__(self):
        return self.body[:20]
    # 追記
    def liked_user_ids(self):
        return [liked_user.id for liked_user in self.liked_users.all()]
        
# Comment モデルを追加
class Comment(models.Model):
    body = models.CharField("本文", max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="投稿者")
    photo = models.ForeignKey(Photo, on_delete=models.PROTECT, verbose_name="コメント先の投稿")
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
 
    def __str__(self):
        return f"{self.user.username}: {self.body[:20]}"
        

    