from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        # Si l'utilisateur est connecté, rediriger vers le flux
        if request.user.is_authenticated:
            return redirect('feed')
        # Sinon, afficher la page d'accueil standard
        return super().get(request, *args, **kwargs)

class SignupView(View):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # Redirect to home page after successful signup
        return render(request, self.template_name, {'form': form})
