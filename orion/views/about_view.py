
from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "about.html")
