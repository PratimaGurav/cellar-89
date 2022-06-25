from allauth.account.forms import SignupForm
from django import forms
from django.forms import ValidationError
 
 
class CustomSignupForm(SignupForm):
    over_18 = forms.BooleanField(help_text='Please confirm you are over 18')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.over_18 = self.cleaned_data['over_18']
        if user.over_18 is not True:
            raise ValidationError('You are restricted from registering.\
                                                  Please contact admin.')
        user.save()
        return user