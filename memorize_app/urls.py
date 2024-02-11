from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", views.index),
    path("login/", views.login),
    path("registration/", views.registration),
    path(
        "success_registration/",
        TemplateView.as_view(template_name="memorize_app/success_registration.html"),
    ),
]
