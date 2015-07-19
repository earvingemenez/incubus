from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import LoginForm
from .mixins import AuthenticationMixin


class IndexView(TemplateView):
    """ Class based view for the index page
    """
    template_name = 'main/index.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class LoginView(AuthenticationMixin, TemplateView):
    """ Class based view that handles the user authentication. this evaluates the user's
        inputted username and password and authenticate it using `LoginForm` which is an
        extension of django's AuthenticationForm.
    """
    template_name = 'main/login.html'
    context = {}

    def get(self, *args, **kwargs):
        self.context['form'] = LoginForm()
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        data = self.request.POST
        form = LoginForm(data=data)

        # calls the validation method of
        # `django.contrib.auth.forms.AuthenticationForm`
        if form.is_valid():
            # `form.get_user()` is a method from
            # `django.contrib.auth.forms.AuthenticationForm`
            self.login(form.get_user())
            # If next attribute is available
            next_ = self.request.GET.get('next')
            return HttpResponseRedirect(self.redirect_to(next_))
        else:
            # form is not valid meaning that username/password is invalid
            # or user doesn't not exists in the database.
            self.context['form'] = form
            return render(self.request, self.template_name, self.context)


class DashboardView(TemplateView):
    """ Class based view for the user's dashboard
    """
    template_name = 'main/dashboard.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)