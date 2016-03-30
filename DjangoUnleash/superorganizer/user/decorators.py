from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.utils.decorators import available_attrs
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def custom_login_required(view):
    @wraps(view, assigned=available_attrs(view))
    def new_view(request, *args, **kwargs):
        user = get_user(request)
        if user.is_authenticated():
            return view(request, *args, **kwargs)
        else:
            url = '{}?next={}'.format(
                settings.LOGIN_URL,
                request.path)
            return redirect(url)

    return new_view
    # decorator = method_decorator(login_required)
    # decorated_view = decorator(view)
    # return decorated_view
