from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def save(self, commit=True, author=None):
        instance = super(PostForm, self).save(commit=False)
        if author:
            instance.author = author
        if commit:
            instance.save()
        return instance
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title