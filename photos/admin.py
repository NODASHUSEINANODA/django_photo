from django.contrib import admin
from .models import Photo, Comment # 追記
 
admin.site.register(Photo)
admin.site.register(Comment) # 追記