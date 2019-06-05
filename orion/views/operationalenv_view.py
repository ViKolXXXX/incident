
from django.shortcuts import render
from django.views.generic import TemplateView


class OperationalEnvView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "operationalenv.html")
