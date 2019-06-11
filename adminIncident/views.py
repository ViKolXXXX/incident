from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from incidentProject.mixins import GroupRequiredMixin


class AdminIncidentView(GroupRequiredMixin, TemplateView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        all_users = User.objects.all()
        context = {"all_users": all_users}
        return render(request, "adminincident.html", context)


class DeleteUserView(GroupRequiredMixin, TemplateView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        User.objects.get(id=self.kwargs['id_user']).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeUserView(GroupRequiredMixin, TemplateView):
    group_required = ['orion']
    template_name = "changeuser.html"

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        print(type(user_id))
        print(user_id)
        if user_id.isdigit():
            user = User.objects.get(id=user_id)
            context = {"user": user}
            return render(request, self.template_name, context)
        else:
            return HttpResponseNotFound('<h1>Нет такой страницы</h1>')

    def post(self, request, *args, **kwargs):
        print(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
