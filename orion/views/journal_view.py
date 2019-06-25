from django.shortcuts import render
from django.views.generic import TemplateView

from orion.models import Event
from orion.views.abstract.orion_view import OrionView


class JournalView(OrionView):
    group_required = ['orion']
    template_name = "journal.html"

    def get(self, request, *args, **kwargs):
        print(request.user.userprofile.subdivision)
        context = {
            "events": Event.available_requests(request.user.userprofile.subdivision.name)
        }
        return render(request, self.template_name, context)
