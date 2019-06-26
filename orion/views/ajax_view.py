from django.http import JsonResponse

from orion.models import Event
from orion.views.abstract.orion_view import OrionView


class CountEventView(OrionView):
    group_required = ['orion']
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
