from allauth.account.forms import SignupForm
from datetime import date

class CustomSignUpForm(SignupForm):
    birthday = forms.DateField()

    def clean_birthday(self):
        dob = self.cleaned_data['birthday']
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('You must be at least 18 years old to sign up')
        return dob

    class Meta:
        fields = ('email', 'username', 'password1', 'password2', 'date_of_birth')