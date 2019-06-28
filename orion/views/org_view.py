from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from orion.models import Org
from orion.views.abstract.orion_view import OrionView
from orion.forms import OrgForm


class OrgView(OrionView):
    group_required = ['Орион']
    template_name = "org.html"

    def get(self, request, *args, **kwargs):
        context = {
            "orgs": Org.objects.all(),
        }
        return render(request, self.template_name, context)


class AddOrgView(OrionView):
    group_required = ['Орион']
    template_name = "org_content_modal_add.html"

    def get(self, request, *args, **kwargs):
        context = {"org_form": OrgForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            org_form = OrgForm(request.POST)
            if org_form.is_valid():
                org_form.save()
                messages.success(request, "Данные успешно сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Данные не сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeOrgView(OrionView):
    group_required = ['Орион']
    template_name = "org_content_modal_change.html"

    def get(self, request, *args, **kwargs):
        org_id = request.GET.get("org_id")
        org = Org.objects.get(id=org_id)
        org_form = OrgForm(None, instance=org)
        context = {"org_form": org_form, "org_id": org_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            org_id = request.POST.get("org_id")
            org = Org.objects.get(id=org_id)
            org_form = OrgForm(request.POST, instance=org)
            if org_form.is_valid():
                org_form.save()
                messages.success(request, "Данные успешно сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Данные не сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteOrgView(OrionView):
    group_required = ['Орион']
    template_name = "org.html"

    def get(self, request, *args, **kwargs):
        try:
            org_id = request.GET.get("org_id")
            Org.objects.get(id=org_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except ProtectedError:
            messages.error(request, "Нельзя удалить, используется!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
