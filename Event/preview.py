from django.http import HttpResponseRedirect

from formtools.preview import FormPreview
from .models import user_data

class userformPreview(FormPreview):
    preview_template    = 'preview.html'
    form_template       = 'registration.html'

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('/form/success')