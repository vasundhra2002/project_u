# blog/forms.py
from django import forms
from .models import BlogPost
from django.contrib.auth.models import User

# Form for creating and editing BlogPost
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']

    #Sset the current logged-in user as the default for the author
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user
        super().__init__(*args, **kwargs)
        if user:
            self.fields['author'].initial = user
        self.fields['author'].queryset = User.objects.all()  # Ensure the form shows all users
