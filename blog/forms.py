from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Enter blog title'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select shadow-sm w-25'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a short summary'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write full content'}),
            'is_draft': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
