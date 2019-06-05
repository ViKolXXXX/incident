
from django.shortcuts import render
from django.views.generic import TemplateView


class JournalView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "journal.html")
