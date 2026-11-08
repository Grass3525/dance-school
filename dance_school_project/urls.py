from django.contrib import admin
from django.urls import include, path

from dance_school_project import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("admin/", admin.site.urls),
    path("school/", include("schoolmanagement.urls")),
    path("school-conf/", include("school.urls")),
    path("api/v1/example/", views.api_example, name="api_example"),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]
