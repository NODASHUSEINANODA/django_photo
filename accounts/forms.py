from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm, # 追記
)
from django.contrib.auth import get_user_model
 
User = get_user_model()
 
class SignupForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    class Meta:
        model = User
        fields = ("username",)
        
class LoginForm(AuthenticationForm):
    pass
    # 継承のみ