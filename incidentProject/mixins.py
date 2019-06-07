from django.contrib import messages, redirects
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


class GroupRequiredMixin(object):

    group_required = None

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, '1')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            user_groups = []
            for group in request.user.groups.values_list('name', flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                messages.add_message(request, messages.INFO, '1')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return super().dispatch(request, *args, **kwargs)