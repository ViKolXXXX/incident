from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import TypeMessage, Titul, Organizatsiya, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import EventForm, TitulForm, OrganizatsiyaForm


class OrganizationView(OrionView):
    group_required = ['orion']
    template_name = "organizatsiya.html"

    def get(self, request, *args, **kwargs):
        context = {
            "organizatsiya_form": OrganizatsiyaForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        organizatsiya_form = OrganizatsiyaForm(request.POST)
        if organizatsiya_form.is_valid():
            organizatsiya_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            context = {"organizatsiya_form": organizatsiya_form}
            return render(request, self.template_name, context)
