from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HeadOrionView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "headorion.html")
