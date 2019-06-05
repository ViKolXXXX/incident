from abc import abstractclassmethod, ABC

from django.views import View
from django.views.generic import TemplateView

from incidentProject.mixins import GroupRequiredMixin


class OrionView(ABC, GroupRequiredMixin, TemplateView):
    pass

