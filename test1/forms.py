from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db import transaction

from .models import User

# User Creation Form

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'national_id', 'username']
        field_classes = {"username": UsernameField}

    @transaction.atomic
    def save(self, commit=False):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        user.save()
        return user