from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    # path("",views.main,name="main"),
    # path("login", views.login, name="login"),
    # path("register", views.register, name="register"),
    path("index/", views.index, name="index"),
    path("", views.index, name="index"),
    path("index/index", views.index, name="index"),

    path("index/create-resume", views.create_resume, name="create-resume"),
    path("create-resume/", views.create_resume, name="create-resume"),
    path("resume", views.resume, name="resume"),
    path("index/resume", views.resume, name="resume"),


]
