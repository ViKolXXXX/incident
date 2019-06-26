from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from orion.models import Event
from orion.views.abstract.orion_view import OrionView


class AnalyticsView(OrionView):
    group_required = ['orion']
    def get(self, request, *args, **kwargs):
        context = {"all_event" : Event.objects.all().count()}
        return render(request, "analytics.html", context)


