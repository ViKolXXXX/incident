from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from orion.models import Event
from orion.views.abstract.orion_view import OrionView


class JournalView(OrionView):
    group_required = ['Орион']
    template_name = "journal.html"

    def get(self, request, *args, **kwargs):
        try:
            events = Event.available_requests(request.user.userprofile.subdivision.pk)
            return render(request, self.template_name, {"events": events})

        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

