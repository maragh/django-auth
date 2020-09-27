from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'