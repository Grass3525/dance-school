from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

__all__ = [
    "SignUpView",
    "about",
    "api_example",
    "home",
]


def home(request):
    return render(request, template_name="home.html")


def about(request):
    return render(
        request,
        template_name="about.html",
    )


def api_example(request):
    data = {
        "name": "Mattia",
        "email": "m.grassotti@itsolivetti.it",
    }
    return JsonResponse(data)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # dopo la registrazione l'utente è già dentro
        return response
