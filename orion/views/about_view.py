
from django.shortcuts import render
from django.views.generic import TemplateView

from orion.views.abstract.orion_view import OrionView


class AboutView(OrionView):
    group_required = ['Орион']
    def get(self, request, *args, **kwargs):
        return render(request, "about.html")
