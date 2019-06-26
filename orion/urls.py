from django.contrib.auth.decorators import login_required
from django.urls import re_path, path, include

from orion.views import headorion_view, event_view, operationalenv_view, face_view, journal_view, analytics_view, about_view, titul_view, organization_view, ajax_view

urlpatterns = [

    re_path(r'^headorion$', login_required(headorion_view.HeadOrionView.as_view()), name="headorion"),
    re_path(r'^event/', include([
        re_path(r'^$', event_view.EventView.as_view(), name="event"),
        re_path(r'^change$', event_view.ChangeEventView.as_view(), name="change_event"),
        re_path(r'^delete$', event_view.DeleteEventView.as_view(), name="delete_event"),
    ])),
    re_path(r'^face/', include([
        re_path(r'^$', face_view.FaceView.as_view(), name="face"),
        re_path(r'^change$', face_view.ChangeFaceView.as_view(), name="change_face"),
        re_path(r'^delete$', face_view.DeleteFaceView.as_view(), name="delete_face"),
    ])),
    re_path(r'^titul/', include([
        re_path(r'^$', titul_view.TitulView.as_view(), name="titul"),
        re_path(r'^change$', titul_view.ChangeTitulView.as_view(), name="change_titul"),
        re_path(r'^delete$', titul_view.DeleteTitulView.as_view(), name="delete_titul"),
    ])),
    re_path(r'^organizatsiya/', include([
        re_path(r'^$', organization_view.OrganizationView.as_view(), name="organizatsiya"),
        re_path(r'^change$', organization_view.ChangeOrganizationView.as_view(), name="change_organizatsiya"),
        re_path(r'^delete$', organization_view.DeleteOrganizationView.as_view(), name="delete_organizatsiya"),
    ])),
    re_path(r'^operationalenv/', include([
        re_path(r'^$', operationalenv_view.OperativnayaObstanovkaView.as_view(), name="operationalenv"),
        re_path(r'^change$', operationalenv_view.ChangeOperativnayaObstanovkaView.as_view(), name="change_operationalenv"),
        re_path(r'^delete$', operationalenv_view.DeleteOperativnayaObstanovkaView.as_view(), name="delete_operationalenv"),
    ])),
    re_path(r'^journal$', login_required(journal_view.JournalView.as_view()), name="journal"),
    re_path(r'^anlytics$', login_required(analytics_view.AnalyticsView.as_view()), name="analytics"),
    re_path(r'^about$', login_required(about_view.AboutView.as_view()), name="about"),

    # AJAX
    re_path(r'^count_event/', login_required(ajax_view.CountEventView.as_view()), name="count_event"),

]
