from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, update_session_auth_hash
from django.shortcuts import render, redirect
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


class PasswordChangeView(FormView):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'passwordchange.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Пароль успешно изменен!!!")
            return redirect('logout')
        else:
            messages.error(request, "Пароль не изменен!!!")
            return render(request, 'passwordchange.html', {'form': form})
