from .models import Post
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
          'image',
          'caption'
        ]