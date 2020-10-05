from django.views.generic import TemplateView
from django.apps import apps

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls', 'books']
        verbose_dict = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                verbose_dict[app.label] = app.verbose_name
        context['verbose_dict'] = verbose_dict
        return context
