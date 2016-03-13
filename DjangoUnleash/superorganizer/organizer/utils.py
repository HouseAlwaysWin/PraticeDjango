from django.shortcuts import (redirect,
                              render,
                              get_object_or_404)
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Model
