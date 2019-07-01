from django.http import JsonResponse
from django.shortcuts import render

from orion.forms import EventForm, TitulForm
from orion.models import Event, Titul
from orion.views.abstract.orion_view import OrionView
from django.forms import inlineformset_factory


class CountEventView(OrionView):
    group_required = ['Орион']
    regions = {"ОСБ ЦО": "Центральный федеральный округ",
               "ОСБ СЗО": "Северо-Западный федеральный округ",
               "ОСБ ЮО": "Южный федеральный округ",
               "ОСБ СКО": "Северо-Кавказкий федеральный округ",
               "ОСБ ПривО": "Приволжский федеральный округ",
               "ОСБ УрО": "Уральский федеральный округ",
               "ОСБ СибО": "Сибирский федеральный округ",
               "ОСБ ВО": "Восточный федеральный округ"
               }

    def get(self, request, *args, **kwargs):
        region = request.GET.get("region")
        for key, items in self.regions.items():
            if items == region:
                element = Event.objects.filter(subdivision__name=key).count()
                break
            else:
                element = 0
        context = {"element": element}
        return JsonResponse(context)


class ShowEventView(OrionView):
    group_required = ['Орион']

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get("event_id")
        event = Event.available_request(request.user.userprofile.subdivision.pk, event_id)
        # event_form = EventForm(None, instance=event)
        context = {"event": event}
        return render(request, "event_body_modal.html", context)
