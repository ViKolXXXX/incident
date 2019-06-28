from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from orion.views.abstract.orion_view import OrionView


class HeadOrionView(OrionView):
    group_required = ['Орион']
    def get(self, request, *args, **kwargs):
        return render(request, "headorion.html")
