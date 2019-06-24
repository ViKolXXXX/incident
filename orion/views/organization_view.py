from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from orion.models import Organizatsiya
from orion.views.abstract.orion_view import OrionView
from orion.forms import OrganizatsiyaForm


class OrganizationView(OrionView):
    group_required = ['orion']
    template_name = "organizatsiya.html"

    def get(self, request, *args, **kwargs):
        context = {
            "organizatsii": Organizatsiya.objects.all(),
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
            context = {"organizatsii": Organizatsiya.objects.all(), "organizatsiya_form": organizatsiya_form}
            messages.error(request, "Данные не сохранены!!!")
            return render(request, self.template_name, context)


class ChangeOrganizationView(OrionView):
    group_required = ['orion']
    template_name = "organizatsiya_change.html"

    def get(self, request, *args, **kwargs):
        organizatsiya_id = request.GET.get("organizatsiya_id")
        organizatsiya = Organizatsiya.objects.get(id=organizatsiya_id)
        organizatsiya_form = OrganizatsiyaForm(None, instance=organizatsiya)

        context = {"organizatsiya_form": organizatsiya_form, "organizatsiya_id": organizatsiya_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        organizatsiya_id = request.POST.get("organizatsiya_id")
        organizatsiya = Organizatsiya.objects.get(id=organizatsiya_id)
        organizatsiya_form = OrganizatsiyaForm(request.POST, instance=organizatsiya)
        if organizatsiya_form.is_valid():
            organizatsiya_form.save()
            messages.success(request, "Данные успешно сохранены!!!")
            context = {"organizatsiya_form": OrganizatsiyaForm()}
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            context = {"organizatsiya_form": organizatsiya_form}
            messages.error(request, "Данные не сохранены!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteOrganizationView(OrionView):
    group_required = ['orion']
    template_name = "organizatsiya.html"

    def get(self, request, *args, **kwargs):
        try:
            organizatsiya_id = request.GET.get("organizatsiya_id")
            Organizatsiya.objects.get(id=organizatsiya_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
