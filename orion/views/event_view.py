from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import TypeMessage, Event, Org, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import EventForm, EventForm


class EventView(OrionView):
    group_required = ['Орион']
    template_name = "event.html"

    def get(self, request, *args, **kwargs):
        context = {
            "event_form": EventForm(),
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

class ChangeEventView(OrionView):
    group_required = ['Орион']
    template_name = "event_change.html"

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get("event_id")
        event = Event.available_request(request.user.userprofile.subdivision.pk, event_id)
        event_form = EventForm(None, instance=event)

        context = {"event_form": event_form, "event_id": event_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        event_id = request.POST.get("event_id")
        event = Event.available_request(request.user.userprofile.subdivision.pk, event_id)
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save(commit=False)
            event_form.user = request.user
            event_form.subdivision = request.user.userprofile.subdivision
            event_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Данные не сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteEventView(OrionView):
    group_required = ['Орион']
    template_name = "journal.html"

    def get(self, request, *args, **kwargs):
        try:
            event_id = request.GET.get("event_id")
            Event.available_request(request.user.userprofile.subdivision.pk, event_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))