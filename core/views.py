from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from core.forms import ContactForm
from core.models import Employee, Service


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)
        context['employees'] = Employee.objects.filter(is_active=True)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, "E-mail enviado com sucesso")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar formulário")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
