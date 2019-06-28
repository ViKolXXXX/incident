from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import OperativnayaObstanovka
from orion.views.abstract.orion_view import OrionView
from orion.forms import OperationalEnvForm


class OperationalEnvView(OrionView):
    group_required = ['Орион']
    template_name = "operationalenv.html"

    def get(self, request, *args, **kwargs):
        context = {
            "operationalenvs": OperativnayaObstanovka.objects.all(),
        }
        return render(request, self.template_name, context)


class AddOperationalEnvView(OrionView):
    group_required = ['Орион']
    template_name = "operationalenv_content_modal_add_.html"

    def get(self, request, *args, **kwargs):
        context = {"operationalenv_form": OperationalEnvForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            operationalenv_form = OperationalEnvForm(request.POST)
            if operationalenv_form.is_valid():
                operationalenv_form.save()
                messages.success(request, "Данные успешно сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Данные не сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeOperationalEnvView(OrionView):
    group_required = ['Орион']
    template_name = "operationalenv_content_modal_change.html"

    def get(self, request, *args, **kwargs):
        operationalenv_id = request.GET.get("operationalenv_id")
        operationalenv = OperativnayaObstanovka.objects.get(id=operationalenv_id)
        operationalenv_form = OperationalEnvForm(None, instance=operationalenv)
        context = {"operationalenv_form": operationalenv_form, "operationalenv_id": operationalenv_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            operationalenv_id = request.POST.get("operationalenv_id")
            operationalenv = OperativnayaObstanovka.objects.get(id=operationalenv_id)
            operationalenv_form = OperationalEnvForm(request.POST, instance=operationalenv)
            if operationalenv_form.is_valid():
                operationalenv_form.save()
                messages.success(request, "Данные успешно сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Данные не сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteOperationalEnvView(OrionView):
    group_required = ['Орион']
    template_name = "operationalenv.html"

    def get(self, request, *args, **kwargs):
        try:
            operationalenv_id = request.GET.get("operationalenv_id")
            OperativnayaObstanovka.objects.get(id=operationalenv_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except ProtectedError:
            messages.error(request, "Нельзя удалить, используется!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))