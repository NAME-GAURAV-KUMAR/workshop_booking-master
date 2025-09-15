# Django Imports
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

# Local Imports
from cms.models import Page


def index(request):
    # Check if user is authenticated and redirect accordingly
    if request.user.is_authenticated:
        # Redirect authenticated users to their dashboard
        redirect_url = reverse("workshop_app:index")
    else:
        # Show the modern home page to unauthenticated users
        redirect_url = reverse("workshop_app:home")
    return redirect(redirect_url)
