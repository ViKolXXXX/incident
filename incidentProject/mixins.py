from django.contrib import messages, redirects
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


class GroupRequiredMixin(object):

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, '1')
        if not request.user.is_authenticated:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            user_groups = []
            for group in request.user.groups.values_list('name', flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return GroupRequiredMixin.dispatch(request, *args, **kwargs)