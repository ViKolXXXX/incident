
from django.urls import re_path, path

from adminIncident.views import AdminIncidentView, DeleteUserView, ChangeUserView

urlpatterns = [
    re_path(r'^$', AdminIncidentView.as_view(), name="adminincident"),
    re_path(r'^delete/(?P<id_user>\d+)$', DeleteUserView.as_view(), name="deleteuser"),
    re_path(r'^change/$', ChangeUserView.as_view(), name="change_user"),


    # re_path(r'^change/(?P<user_id>\d+)/$', ChangeUserView.as_view(), name="change_user"),



    # re_path(r'^headorion$', login_required(headorion_view.HeadOrionView.as_view()), name="headorion"),
    # re_path(r'^event$', login_required(event_view.EventView.as_view()), name="event"),
    # re_path(r'^operationalenv$', login_required(operationalenv_view.OperationalEnvView.as_view()), name="operationalenv"),
    # re_path(r'^face$', login_required(face_view.FaceView.as_view()), name="face"),
    # re_path(r'^journal$', login_required(journal_view.JournalView.as_view()), name="journal"),
    # re_path(r'^anlytics$', login_required(analytics_view.AnalyticsView.as_view()), name="analytics"),
    # re_path(r'^about$', login_required(about_view.AboutView.as_view()), name="about"),


]

