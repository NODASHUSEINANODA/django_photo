from django.urls import path
from . import views
 
app_name = "accounts"
 
urlpatterns = [
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),
    path("login/", views.Login.as_view(), name="login"), # ログイン
    path("logout/", views.Logout.as_view(), name="logout"), # ログアウト
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # ユーザー詳細
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("follow/<int:pk>/", views.follow, name="follow"),
    path("unfollow/<int:pk>/", views.unfollow, name="unfollow"),
]