from django import forms
from .models import UserProfile

from allauth.account.forms import SignupForm
from datetime import date

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            self.fields[field].label = False


class CustomSignUpForm(SignupForm):
    date_of_birth = forms.DateField()

    def clean_birthday(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('You must be at least 18 years old to register')
        return dob

    class Meta:
        model = UserProfile
        fields = ('date_of_birth')