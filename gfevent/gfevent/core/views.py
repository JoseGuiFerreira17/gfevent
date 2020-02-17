from django.views.generic import TemplateView

# Create your views here.


class BlankPageView(TemplateView):
    template_name = 'core/index.html'
