from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Startups, NewsLink


class SlugCleanMixin:

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug


class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class StartupForm(SlugCleanMixin,forms.ModelForm):

    class Meta:
        model = Startups
        fields = '__all__'


class NewsLinkForm(SlugCleanMixin,forms.ModelForm):
    
    class Meta:
        model = NewsLink
        fields = '__all__'

    def save(self, **kwargs):
        
        instance = super().save(commit=False)
        instance.startup = (
            self.data.get('startup'))
        instance.save()
        self.save_m2m()

        return instance

    def clean(self):
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug')
        startup_obj = self.data.get('startup')
        exists = (NewsLink.objects.filter(
            slug__iexact=slug,
            startup=startup_object,).exists())
        if exists:
            reise ValidationError(
                "News articles with this Slug"
                "and Startup already exists.")
        else:
            return cleaned_data
