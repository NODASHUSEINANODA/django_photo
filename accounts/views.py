from django.shortcuts import render, redirect, get_object_or_404 # 追記
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin # 追記
from django.contrib.auth import get_user_model
import random
 
from .forms import SignupForm, LoginForm
from photos.models import Photo
from .models import Followership # 追記
 
 
class SignUp(generic.CreateView):
    model = Photo
    """サインアップ"""
    form_class = SignupForm
    template_name = "accounts/sign_up.html"
 
    def get_success_url(self):
        return reverse_lazy("photos:index")
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー登録"
        return context
 
 
class Login(LoginView):
    model = Photo
    form_class = LoginForm
    template_name = "accounts/login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログイン"
        return context
 
# ログアウト
class Logout(LogoutView):
    model = Photo
    template_name = "accounts/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログアウトしました"
        return context
 
# ユーザープロフィール
class Detail(LoginRequiredMixin, generic.DetailView):
    model = Photo
    template_name = "accounts/detail.html"
    # context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プロフィール"
        # ここに6章課題の処理
        return context
 
# ユーザープロフィールの更新
class Update(LoginRequiredMixin, generic.UpdateView):
    model = Photo
    template_name = "accounts/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プロフィール編集"
        return context
        
        
def follow(request,pk):
    model = Photo
    user = get_object_or_404(get_user_model(), pk=pk)
    Followership.objects.get_or_create(follower=request.user, followee=user)
    return redirect("photos:index")
 
def unfollow(request,pk):
    model = Photo
    user = get_object_or_404(get_user_model(), pk=pk)
    Followership.objects.get(follower=request.user, followee=user).delete()
    return redirect("photos:index")
    
def like(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    request.user.likes.add(photo)
    return redirect("photos:index")
 
def dislike(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    request.user.likes.remove(photo)
    return redirect("photos:index")