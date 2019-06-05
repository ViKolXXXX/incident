
from django.shortcuts import render
from django.views.generic import TemplateView


class AdminView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "admin.html")
