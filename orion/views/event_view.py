
from django.shortcuts import render
from django.views.generic import TemplateView

from orion.views.abstract.orion_view import OrionView


class EventView(OrionView):
    group_required = ['admin']
    def get(self, request, *args, **kwargs):
        return render(request, "event.html")
