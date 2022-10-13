from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy # 追記
# 追記
from .models import Photo, Comment # 追記
from .forms import PhotoCreateForm, CommentCreateForm # 追記
from django.contrib.auth import get_user_model
import random
 
class Index(LoginRequiredMixin, generic.ListView):
    template_name = "photos/index.html"
    model = Photo
    ordering = "-created_at"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "トップ"
        User = get_user_model()
        recommended_users = list(User.objects.all().exclude(id=self.request.user.id)[:30])
        if len(recommended_users) > 3:
            recommended_users = random.sample(recommended_users, 3)
        context["recommended_users"] = recommended_users
        return context
 
    def get_queryset(self):
        queryset = super().get_queryset()
        timeline_ids = self.request.user.follows_ids()
        timeline_ids.append(self.request.user.id)
        queryset = queryset.filter(user_id__in=timeline_ids)
        return queryset
 
class Create(LoginRequiredMixin, generic.CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = "photos/create.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "投稿の新規作成"
        return context
 
    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        return redirect("photo:index")
 
class Detail(LoginRequiredMixin, generic.DetailView):
    model = Photo
    template_name = "photos/detail.html"
    context_object_name = 'profile_user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "投稿詳細"
        return context
 
class Update(LoginRequiredMixin, generic.UpdateView):
    model = Photo
    form_class = PhotoCreateForm
    success_url = reverse_lazy("photos:index")
    template_name = "photos/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "投稿の編集"
        return context
        
class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Photo
    success_url = reverse_lazy("photos:index")
    
    
class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "コメントの新規作成"
        return context
 
    def form_valid(self, form):
        photo_pk = self.kwargs["pk"]
        photo = get_object_or_404(Photo, pk=photo_pk)
        comment = form.save(commit=False)
        comment.photo = photo
        comment.user = self.request.user
        comment.save()
        return redirect("photos:detail", pk=photo_pk)
        
        
        
def like(request,pk):
        photo = get_object_or_404(Photo, pk=pk)
        request.user.likes.add(photo)
        return redirect("photos:index")
 
def dislike(request,pk):
        photo = get_object_or_404(Photo, pk=pk)
        request.user.likes.remove(photo)
        return redirect("photos:index")
        

