from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from .models import Contact
from .forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


class ContactView(View):
    template_name = 'contact-us.html'
    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # save form data
            form.save()
            messages.success(self.request, 'Thank You, your form submission has been successful!!')
            return HttpResponseRedirect('/')
        else:
            errors = form.errors
            for error in errors:
                messages.error(self.request, 'Please, enter valid ' + error)
            # print form.errors
            print(form.errors)
            return render(request, self.template_name, {'form': form})