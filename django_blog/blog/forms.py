from django import forms
from .models import Post
from .models import Comment

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
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50}),  # Customize the appearance of the content field
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        # Add custom validation rules if needed
        if len(content) < 10:
            raise forms.ValidationError("Content must be at least 10 characters long.")
        return content