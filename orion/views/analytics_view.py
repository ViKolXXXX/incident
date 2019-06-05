
from django.shortcuts import render
from django.views.generic import TemplateView


class AnalyticsView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "analytics.html")
