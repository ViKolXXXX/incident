from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import TypeMessage, Titul, Organizatsiya, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import EventForm, TitulForm


class EventView(OrionView):
    group_required = ['orion']
    template_name = "event.html"

    def get(self, request, *args, **kwargs):
        context = {
            "event_form": EventForm(),
            "titul_form": TitulForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            post = event_form.save(commit=False)
            post.user = request.user
            post.subdivision = request.user.userprofile.subdivision
            post.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Данные не сохранены!!!")
            context = {"event_form": event_form}
            return render(request, self.template_name, context)

#
# class TitulView(OrionView):
#     group_required = ['orion']
#     template_name = "event.html"
#
#     def post(self, request, *args, **kwargs):
#
#         titul_form = TitulForm(request.POST)
#
#         if titul_form.is_valid():
#             titul_form.save()
#             messages.success(request, "Данные успешно сохранены!!!")
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#         else:
#             messages.error(request, "Форма имеет не правильные значения!!!")
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
