from django.contrib import admin
from django.conf.urls import url
from django.contrib.messages import success
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.html import escape
from django.core.exceptions import PermissionDenied
from django.http import (
    Http404, HttpResponseRedirect)
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.views.decorators.debug import sensitive_post_parameters


from .models import User
from .forms import UserCreationForm



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list view
    list_display = (
        'get_name',
        'email',
        'get_date_joined',
        'is_staff',
        'is_superuser')
    list_filter = (
        'is_staff',
        'is_superuser',
        'profile__joined')
    search_fields = ('email',)
    ordering = ('email',)
    list_display_links = ('get_name','email')

    change_password_form = AdminPasswordChangeForm
    change_user_password_template =(
        'admin/auth/user/change_password.html')
  
   

    # form view
    fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email',)}),
        ('Permissions', {
            'classes':('collapse',),
            'fields':(
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions')}),
        ('Important dates',{
            'classes':('collapse',),
            'fields':('last_login',)}),
        )
    filter_horizontal = ('groups','user_permissions',)

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':(
                'name',
                'email',
                'password1',
                'password2',)
            }),
        )
    add_form = UserCreationForm

    def get_date_joined(self, user):
        return user.profile.joined
    get_date_joined.short_description = 'Joined'
    get_date_joined.admin_order_field = ('profile__joined')

    def get_name(self, user):
        return user.profile.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'profile__name'

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['form']=self.add_form
        return super().get_form(
            request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request,obj)

    def get_urls(self):
        password_change = [
            url(r'^(.+)/password/$',
                self.admin_site.admin_view(
                    self.user_change_password),
                name='auth-user_password_change'),]
        urls = super().get_urls()
        urls = password_change + urls
        return urls

    @method_decorator(sensitive_post_parameters())
    def user_change_password(
            self, request, user_id, form_url=''):
        if not self.has_change_permission(request):
            raise PermissionDenied
        user = self.get_object(
            request,unquote(user_is))
        if user is None:
            raise Http404(
                '{name} object with primary key '
                '{key} does not exist.'.format(
                    name=force_text(
                        self.model._meta.verbose_name),
                    key=escape(user_id)))
        if request.method == 'POST':
            form = self.change_password_form(
                user,request.POST)
        if form.is_valid():
            form.save()
            change_message = (
                self.contruct_change_message(
                    request, form, None))
            self.log_change(request, user, change_message)
            success(request, 'Password changed.')
            update_session_auth_hash(
                request, form.user)
            return HttpResponseRedirect('..')
        
