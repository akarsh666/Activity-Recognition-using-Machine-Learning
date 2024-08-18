from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("abstract", views.abstract, name="abstract"),
    path("prediction", views.prediction, name="prediction"),
    path("prediction2", views.prediction2, name="prediction2"),
    path("performance", views.performance, name="performance"),
]