from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """ Form class that is an extension of `django.contrib.auth.form.AuthenticationForm`.
        This uses the `AuthenticationForm` class to authenticate the User object and set
        custom error message.
        This can also be used if we are going to add rules for authenticating/giving access
        to users.
    """
    error_message = "Username/Password is incorrect. Please try again."

    # added field classes which is dependent to the template
    username = forms.CharField(widget=forms.TextInput({
        'class': 'form-control input-lg',
        'placeholder': 'Username',
        }))
    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'form-control input-lg',
        'placeholder': 'Password',
        }))

    def clean(self):
        # retrieve user data from the form
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Check if username and password is not null.
        if username and password:
            self.user_cache = authenticate(username=username,
                                        password=password)
            # Check if user is null and is not active
            if self.user_cache is None or not self.user_cache.is_active:
                # raise and error
                raise forms.ValidationError(self.error_message,
                                        code='invalid_login')
        else:
            # Either username or password is null. both should have values.
            raise forms.ValidationError(self.error_message,
                                    code='invalid_login')

        return self.cleaned_data