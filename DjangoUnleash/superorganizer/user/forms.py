import logging
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from user.utils import ActivationMailFormMixin
from user.models import Profile

logger = logging.getLogger(__name__)

class UserCreationForm(
        ActivationMailFormMixin,
        BaseUserCreationForm):
    
    mail_validation_error = ('User created. Could not send activation '
                             'email. Please try again later. (Sorry!')

    def save(self, **kwargs):
        user = super().save(commit=False)
        if not user.pk:
            user.is_active = False
            send_mail = True
        else:
            send_mail = False

        user.save()
        self.save_m2m()
        Profile.objects.update_or_create(
            user=user,
            defaults={
                'slug':slugify(
                    user.get_username()),
                })
        
        if send_mail:
            self.send_mail(user=user, **kwargs)
        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = (
            'activate',
            'create',
            'disable',
            'login',
            'logout',
            'password',
            'profile',
            )
        if username in disallowed:
            raise ValidaionError(
                "A user with that username"
                " already exists"
                )
        return username

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email')

class ResendActivationEmailForm(
        ActivationMailFormMixin,forms.Form):
    email = forms.EmailField()

    mail_validation_error = (
        'Could not re-send activation email'
        'Please try again later.')

    def save(self,**kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(
                email=self.cleaned_data['email'])
        except:
            logger.warning(
                'Resend Activation: No user with '
                'email: {}.'.format(
                    self.cleaned_data['email']))
            return None
        self.send_mail(user=user,**kwargs)
        return user
