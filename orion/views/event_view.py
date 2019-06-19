from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import TypeMessage, Titul, Organizatsiya, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import EventForm


class EventView(OrionView):
    group_required = ['orion']
    template_name = "event.html"

    def get(self, request, *args, **kwargs):
        context = {
            # "type_messages": TypeMessage.objects.all(),
            # "tituls": Titul.objects.all(),
            # "organizatsii": Organizatsiya.objects.all(),
            # "klassif_priznaki_UK": KlassifPriznakUK.objects.all(),
            # "klassif_priznaki_ugroza": KlassifPriznakUgroza.objects.all(),
            # "faces": Face.objects.all(),
            # "types_proverki": TypeProverki.objects.all(),
            # "rezults_proverki": ResultProverki.objects.all(),
            # "operativnaye_obstanovki": OperativnayaObstanovka.objects.all(),
            "event_form": EventForm()
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     try:
    #         # user_id = request.POST.get("user_id")
    #         # user = User.objects.get(id=user_id)
    #         # user.first_name = request.POST.get("first_name")
    #         # user.last_name = request.POST.get("last_name")
    #         # user.email = request.POST.get("email")
    #         # user.groups.set(request.POST.getlist("group"))
    #         # user.save()
    #         # messages.success(request, "Пользователь изменен!!!")
    #         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #     except:
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
