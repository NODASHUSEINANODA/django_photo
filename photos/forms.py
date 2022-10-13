from django import forms
from .models import Photo, Comment
 
class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("body", "image", )
 
# 追記
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ("body",)