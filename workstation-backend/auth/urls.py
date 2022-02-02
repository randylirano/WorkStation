from django.conf.urls import url
from django.urls import path, include

from .views import LoginView, RegisterView

urlpatterns = [
    path("register", RegisterView.as_view()),
]
