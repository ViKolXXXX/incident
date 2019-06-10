from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from orion.views.abstract.orion_view import OrionView


class AdminIncidentView(OrionView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        all_users = User.objects.all()
        context = {"all_users": all_users}
        return render(request, "adminincident.html", context)



class DeleteUserView(OrionView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        User.objects.get(id=self.kwargs['id_user']).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeUserView(OrionView):
    group_required = ['orion']

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['id_user'])
        context = {"user": user}
        return render(request, "changeuser.html", context)

    def post(self, request):
        user = User.objects.get(id=self.kwargs['id_user'])
        context = {"user": user}
        return render(request, "adminincident.html", context)