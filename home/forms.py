from allauth.account.forms import SignupForm
from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomSignUpForm(SignupForm):
    date_of_birth = forms.DateField()

    def clean_birthday(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('You must be at least 18 years old to register')
        return dob

    class Meta:
        model = User
        fields = ('date_of_birth')