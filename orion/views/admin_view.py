
from django.shortcuts import render
from django.views.generic import TemplateView

from orion.views.abstract.orion_view import OrionView


class AdminView(OrionView):
    group_required = ['orion']
    def get(self, request, *args, **kwargs):
        return render(request, "admin.html")
