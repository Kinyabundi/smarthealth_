from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .forms import UserForm
from .models import User

class HomepageView(generic.TemplateView):
    template_name = 'home.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'

class UserRegistrationView(SuccessMessageMixin, generic.TemplateView):
    model = User
    form_class = UserForm
    template_name = 'register.html'
    success_message = 'Account created successfully!'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse(
                reverse_lazy('home')
            )

        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        register_form = UserForm(self.request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=True)
            messages.success(self.request, self.success_message)
            user.save()
            return HttpResponseRedirect(
                reverse_lazy('home')
            )

        return self.render_to_response(
            self.get_context_data(
                register_form=register_form
            )
        )

    def get_context_data(self, **kwargs):
        if 'register_form' not in kwargs:
            kwargs['register_form'] = UserForm
        return super().get_context_data(**kwargs)


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    print()