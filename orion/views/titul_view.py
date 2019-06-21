from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import TypeMessage, Titul, Organizatsiya, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import EventForm, TitulForm


class TitulView(OrionView):
    group_required = ['orion']
    template_name = "titul.html"

    def get(self, request, *args, **kwargs):
        context = {
            "titul_form": TitulForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        titul_form = TitulForm(request.POST)
        if titul_form.is_valid():
            titul_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            context = {"titul_form": titul_form}
            return render(request, self.template_name, context)



