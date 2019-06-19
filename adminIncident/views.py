from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView

from incidentProject.mixins import GroupRequiredMixin
from orion.models import Subdivision


class AdminIncidentView(GroupRequiredMixin, TemplateView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        all_users = User.objects.all().exclude(username='admin')
        context = {"all_users": all_users}
        return render(request, "adminincident.html", context)


class DeleteUserView(GroupRequiredMixin, TemplateView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        try:
            User.objects.get(id=self.kwargs['id_user']).delete()
            messages.success(request, "Пользователь удален!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Что то пошло не так!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeUserView(GroupRequiredMixin, TemplateView):
    group_required = ['orion']
    template_name = "changeuser.html"

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        if not user_id.isdigit():
            return HttpResponseNotFound('<h1>Нет такой страницы</h1>')
        else:
            user = User.objects.get(id=user_id)
            groups = Group.objects.all()
            subdivisions = Subdivision.objects.all()
            context = {"user": user, "groups": groups, "subdivisions": subdivisions}
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            user_id = request.POST.get("user_id")
            user = User.objects.get(id=user_id)
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.groups.set(request.POST.getlist("group"))
            user.userprofile.subdivision_id = request.POST.get("subdivision")
            user.save()
            messages.success(request, "Пользователь изменен!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
