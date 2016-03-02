from django import form
from .models import Post

class PostForm(form.ModelForm):
    class Meta:
        model = Post
        field = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
