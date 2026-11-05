from django.urls import path

from schoolmanagement import views

urlpatterns = [
    path("", views.SchoolListView.as_view(), name="lista_scuole"),
    path("<int:pk>/", views.SchoolDetailView.as_view(), name="dettaglio_scuola"),
]
