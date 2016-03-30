from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect

from django.contrib.auth.decorators import (login_required,
                                            permission_required)
from django.utils.decorators import method_decorator

def custom_login_required(view):
    decorator = method_decorator(login_required)
    decorated_view = decorator(view)
    return decorated_view

def require_authenticated_permission(permission):

    def decorator(view):
        
        check_auth = login_required
        check_perm = (permission_required(
            permission,
            raise_exception=True))
        # double decorator
        decorated_view = (check_auth(
            check_perm(view)))

        return decorated_view

    return decorator

        
