from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView


class ListView(TemplateView):
    model = None
    context_key = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context[self.context_key] = self.get_objects()
        return context

    def get_objects(self):
        return self.model.objects.all()


class FormView(View):
    form_class = None
    template_name = None
    redirect_url = ""
    object = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        return self.get_redirect_url()

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return render(self.request, self.template_name, context)

    def get_redirect_url(self):
        return redirect(self.redirect_url)

    def get_context_data(self, **kwargs):
        return kwargs
