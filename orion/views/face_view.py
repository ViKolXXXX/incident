from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orion.models import Face
from orion.views.abstract.orion_view import OrionView
from orion.forms import FaceForm


class FaceView(OrionView):
    group_required = ['Орион']
    template_name = "face.html"

    def get(self, request, *args, **kwargs):
        context = {
            "faces": Face.objects.all(),
        }
        return render(request, self.template_name, context)


class AddFaceView(OrionView):
    group_required = ['Орион']
    template_name = "face_content_modal_add.html"

    def get(self, request, *args, **kwargs):
        context = {"face_form": FaceForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            face_form = FaceForm(request.POST)
            if face_form.is_valid():
                face_form.save()
                messages.success(request, "Данные успешно сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Данные не сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeFaceView(OrionView):
    group_required = ['Орион']
    template_name = "face_content_modal_change.html"

    def get(self, request, *args, **kwargs):
        face_id = request.GET.get("face_id")
        face = Face.objects.get(id=face_id)
        face_form = FaceForm(None, instance=face)
        context = {"face_form": face_form, "face_id": face_id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            face_id = request.POST.get("face_id")
            face = Face.objects.get(id=face_id)
            face_form = FaceForm(request.POST, instance=face)
            if face_form.is_valid():
                face_form.save()
                messages.success(request, "Данные успешно сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Данные не сохранены!!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteFaceView(OrionView):
    group_required = ['Орион']
    template_name = "face.html"

    def get(self, request, *args, **kwargs):
        try:
            face_id = request.GET.get("face_id")
            Face.objects.get(id=face_id).delete()
            messages.success(request, "Успешно удалено!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except ProtectedError:
            messages.error(request, "Нельзя удалить, используется!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, "Ошибка при удалении!!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
