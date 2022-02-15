from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Nome'), max_length=100)
    email = forms.EmailField(label=_('Email'), max_length=150)
    subject = forms.CharField(label=_('Assunto'), max_length=100)
    message = forms.CharField(label=_('Mensagem'), max_length=500)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f"None: {name}\nE-Mail: {email}\nAssunto: {subject}\nMensagem: {message}"

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email="contato@fusion.com.br",
            to=['contato@fusion.com.br'],
            headers={"Replay-To": email}
        )

        mail.send()
