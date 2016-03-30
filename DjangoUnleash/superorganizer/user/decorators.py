from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View

from django.contrib.auth.decorators import (login_required,
                                            permission_required)
from django.utils.decorators import method_decorator

# Only ask login without permission
def class_login_required(cls):
    if (not isinstance(cls, type) or not issubclass(cls,View)):
        raise ImproperlyConfigured(
            "class_login_required"
            "must be applied to subclass"
            " of View class.")
    decorator = method_decorator(login_required)
    cls.dispatch = decorator(cls.dispatch)
    return cls

# combine login required and permission
def require_authenticated_permission(permission):

    def decorator(cls):
        if (not isinstance(cls, type) or not issubclass(cls, View)):
            raise ImproperlyConfigured(
                "require_authenticated_permission"
                "must be applied to subclasses "
                "of View class.")
        
        check_auth = method_decorator(login_required)
        check_perm = method_decorator(
            (permission_required(
                permission,
                raise_exception=True
            )))
        # double decorator
        cls.dispatch  = (check_auth(
            check_perm(cls.dispatch)))

        return cls

    return decorator

        
