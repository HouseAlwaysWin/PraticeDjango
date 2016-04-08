from django.shortcuts import redirect

from django.contrib.auth import get_user, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator

from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache

from user.forms import (UserCreationForm,
                        ResendActivationEmailForm)
from user.utils import MailContextViewMixin,ActivationMailFormMixin



class DisableAccount(View):
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = ('user/user_confirm_delete.html')

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def get(self, request):
        return TemplateResponse(
            request,
            self.template_name)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def post(self, request):
        user = get_user(request)
        user.set_unusable_password

        user.is_active = False
        user.save()
        logout(request)
        return redirect(self.success_url)



class ActivateAccount(View):
    success_url = reverse_lazy('dj-auth:login')
    template_name = 'user/user_activate.html'

    @method_decorator(never_cache)
    def get(self, request, uidb64, token):
        User = get_uset_model()
        try:
            uid = force_text(
                urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError,ValueError,
                OverflowError,User.DoesNotExist):
            user =None
        if (user is not None
            and token_generator.check_token(user,token)):
            user.is_active = True
            user.save()
            success(
                request,
                'User Activated!'
                'You may now login.')
            return redirect(self.success_url)
        else:
            return TemplateResponse(
                requset,
                self.template_name)
                
            
class CreateAccount(MailContextViewMixin,View):
    form_class = UserCreationForm
    success_url = reverse_lazy(
        'dj-auth:create_done')
    template_name = 'user/user_create.html'

    @method_decorator(csrf_protect)
    def get(self, request):
        return TemplateResponse(
            request,
            self.template_name,
            {'form':self.form_class()})

    @method_decorator(csrf_protect)
    @method_decorator(sensitive_post_parameters(
        'password1','password2'))
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            # not catching returned user
            bound_form.save(**self.get_save_kwargs(request))
            if bound_form.mail_sent:
                return redirect(self.success_url)
            else:
                errs = (
                    bound_from.non_field_errors())
                for err in errs:
                    error(request,err)
                    # TODO: redirect to email resend
            return redirect(
                'dj-auth:resend_activation')

        return TemplateResponse(
            request,
            self.template_name,
            {'form':bound_form})
    
class ResendActivationEmail(
        MailContextViewMixin,View):
    form_class = ResendActivationEmailForm
    success_url = reverse_lazy('dj-auth:login')
    template_name = 'user/resend_activation.html'

    @method_decorator(csrf_protect)
    def get(self, request):
        return TemplateResponse(
            request,
            self.template_name,
            {'form':self.form_class()})

    @method_decorator(csrf_protect)
    def post(self, request):
        bound_form = self.form_class(request.POST)

        if bound_form.is_valid():
            user = bound_form.save(**self.get_save_kwargs(request))

            if (user is not None and not bound_form.mail.sent):
                errs = (
                    bound_form.non_field_errors())
                for err in errs:
                    error(request, err)
                if errs:
                    bound_form.errors.pop(
                        '__all__')
                return TemplateResponse(
                    request,self.template_name,{'form':self.bound_form})


        success(
            request,
            'Activation Email Sent!')

        return redirect(self.success_url)



