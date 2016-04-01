from django.shortcuts import redirect


from django.contrib.auth import get_user, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator

from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from user.forms import UserCreationForm
from user.utils import MailContextViewMixin


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
    @method_decorator(sensitive_post_paramethers(
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

        return TemplateResponse(
            request,
            self.template_name,
            {'form':bound_form})
    
