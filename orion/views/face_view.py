
from django.shortcuts import render
from django.views.generic import TemplateView


class FaceView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "face.html")
