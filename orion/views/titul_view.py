from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import Titul
from orion.views.abstract.orion_view import OrionView
from orion.forms import TitulForm


class TitulView(OrionView):
    group_required = ['orion']
    template_name = "titul.html"

    def get(self, request, *args, **kwargs):
        context = {
            "tituls": Titul.objects.all(),
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
            context = {"titul_form": titul_form, "tituls": Titul.objects.all()}
            messages.error(request, "Данные не сохранены!!!")
            return render(request, self.template_name, context)


class ChangeTitulView(OrionView):
    group_required = ['orion']
    template_name = "titul_change.html"

    def get(self, request, *args, **kwargs):
        titul_id = request.GET.get("titul_id")
        titul = Titul.objects.get(id=titul_id)
        titul_form = TitulForm(None, instance=titul)

        context = {"titul_form": titul_form, "titul_id": titul_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        titul_id = request.POST.get("titul_id")
        titul = Titul.objects.get(id=titul_id)
        titul_form = TitulForm(request.POST, instance=titul)
        if titul_form.is_valid():
            titul_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Данные не сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteTitulView(OrionView):
    group_required = ['orion']
    template_name = "titul.html"

    def get(self, request, *args, **kwargs):
        try:
            titul_id = request.GET.get("titul_id")
            Titul.objects.get(id=titul_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
