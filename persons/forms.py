
# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Theme', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
