from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.shortcuts import render
from django.views.generic.edit import FormView


class RegisterFormView(FormView):

    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(FormView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login/")

class StartView(FormView):
    def get(self, request):

        return render(request, "start.html")
# Create your views here.
# Create your views here.
