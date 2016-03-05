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

    def save(self):
        new_tag = Tag.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'])
        return new_tag

class StartupForm(SlugCleanMixin,forms.ModelForm):

    class Meta:
        model = Startups
        fields = '__all__'


class NewsLinkForm(SlugCleanMixin,forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
