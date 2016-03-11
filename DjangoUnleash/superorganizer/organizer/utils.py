from django.shortcuts import (redirect,
                              render,
                              get_object_or_404)
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured

class DetailView(View):
    context_object_name = ''
    model = None
    template_name = ''
    template_name_suffix ='_detail'

    def get_object(self):
        sluf = self.kwargs.get('slug')
        if slug is None:
            raise AttributeError(
                "{c} expects {p} parameter"
                "from URL pattern.".format(
                    c=self.__class__.__name__,
                    p='slug'))
        if self.model:
            get_object_or_404(
                self.model,
                slug__iexact=slug)
        else:
            raise ImproperlyConfigured(
                "{c} needs {a} attrubute"
                "specified to work.".format(
                    c=self.__class__.__name__,
                    a='model'))
        
    def get_context_data(self):
        context = {}
        if self.object:
            context_object_name = (
                self.get_context_object_name())
            if context_object_name:
                context[context_object_name] = (
                    self.object)
        return context
    
    def get_template_names(self):
        if self.template_name:
            return self.template_name
        return "{app}/{model}{suffix}.html".format(
            app=self.object._meta.model_name,
            model=self.object._meta.model_name,
            suffix=self.template_name_suffix)
    
    def get_context_object_name(self):
        if self.context_object_name:
            return self.context_object_name
        elif isinstance(self.object, Model):
            return self.object._meta.model_name
        else:
            return None
        
    def get(self, request, slug):
        obj = get_object_or_404(
            self.model,
            slug__iexact=slug)
        return render(
            request,
            self.template_name,
            {self.context_object_name:obj})

class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form':self.form_class()})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form})

class ObjectUpdateMixin:
    form_class = None
    model = None
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model,slug__iexact=slug)
        context = {
            'form':self.form_class(instance=obj),
            self.model.__name__.lower():obj,}
        return render(
            request,
            self.template_name,
            context)

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        bound_form = self.form_class(
            request.POST, instance=obj)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form':bound_form,
                self.model.__name__.lower(): obj,}
            return render(
                request,
                self.template_name,
                context)

class ObjectDeleteMixin:
    model = None
    success_url =''
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        context = { self.model.__name__.lower(): obj,}
        return render(
            request,
            self.template_name,
            context)

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        obj.delete()
        return HttpResponseRedirect(self.success_url)
