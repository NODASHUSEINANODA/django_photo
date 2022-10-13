from django.urls import path
from . import views
 
app_name = "photos"

urlpatterns = [
    path("", views.Index.as_view(), name="index"), # 一覧
    path("create/", views.Create.as_view(), name="create"), # 新規作成
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # 詳細
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("delete/<int:pk>/", views.Delete.as_view(), name="delete"), # 削除
    path("comment/<int:pk>/", views.CommentCreate.as_view(), name="comment_create"),
    path("like/<int:pk>/", views.like, name="like"),
    path("dislike/<int:pk>/", views.dislike, name="dislike"),
]