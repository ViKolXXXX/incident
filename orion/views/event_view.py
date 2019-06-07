
from django.shortcuts import render
from orion.views.abstract.orion_view import OrionView


class EventView(OrionView):
    group_required = ['orion']
    def get(self, request, *args, **kwargs):
        return render(request, "event.html")
