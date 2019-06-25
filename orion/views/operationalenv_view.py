from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import OperativnayaObstanovkaForm


class OperativnayaObstanovkaView(OrionView):
    group_required = ['orion']
    template_name = "operationalenv.html"

    def get(self, request, *args, **kwargs):
        context = {
            "oper_obstanovki": OperativnayaObstanovka.objects.all(),
            "oper_obstanovka_form": OperativnayaObstanovkaForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        oper_obstanovka_form = OperativnayaObstanovkaForm(request.POST)
        if oper_obstanovka_form.is_valid():
            oper_obstanovka_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            context = {"oper_obstanovka_form": oper_obstanovka_form, "oper_obstanovki": OperativnayaObstanovka.objects.all()}
            messages.error(request, "Данные не сохранены!!!")
            return render(request, self.template_name, context)


class ChangeOperativnayaObstanovkaView(OrionView):
    group_required = ['orion']
    template_name = "operationalenv_change.html"

    def get(self, request, *args, **kwargs):
        oper_obstanovka_id = request.GET.get("oper_obstanovka_id")
        oper_obstanovka = OperativnayaObstanovka.objects.get(id=oper_obstanovka_id)
        oper_obstanovka_form = OperativnayaObstanovkaForm(None, instance=oper_obstanovka)
        context = {"oper_obstanovka_form": oper_obstanovka_form, "oper_obstanovka_id": oper_obstanovka_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        oper_obstanovka_id = request.POST.get("oper_obstanovka_id")
        oper_obstanovka = OperativnayaObstanovka.objects.get(id=oper_obstanovka_id)
        oper_obstanovka_form = OperativnayaObstanovkaForm(request.POST, instance=oper_obstanovka)
        if oper_obstanovka_form.is_valid():
            oper_obstanovka_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Данные не сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteOperativnayaObstanovkaView(OrionView):
    group_required = ['orion']
    template_name = "operationalenv.html"

    def get(self, request, *args, **kwargs):
        try:
            oper_obstanovka_id = request.GET.get("oper_obstanovka_id")
            OperativnayaObstanovka.objects.get(id=oper_obstanovka_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
