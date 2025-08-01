# mailer/forms.py
from django import forms

class EmailSendForm(forms.Form):
    to_email = forms.EmailField(label='To Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
