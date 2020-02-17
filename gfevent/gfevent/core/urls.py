from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

from gfevent.core import views

app_name = "core"

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('core:home'))),
    path('home/', views.BlankPageView.as_view(), name="home"),
]
