from django.shortcuts import render
from .bitly_api import shorten_url


def home(request):
    short_url = None
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        if original_url:
            short_url = shorten_url(original_url)
    return render(request, "shortener/home.html", {"short_url": short_url})
