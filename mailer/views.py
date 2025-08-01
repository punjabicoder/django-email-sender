from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import EmailSendForm

def send_email_view(request):
    if request.method == 'POST':
        print("CLASS", EmailSendForm.__module__, type(EmailSendForm))

        form = EmailSendForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            return render(request, 'mailer/success.html')
    else:
        form = EmailSendForm()
    return render(request, 'mailer/send_email.html', {'form': form})

# Create your views here.
