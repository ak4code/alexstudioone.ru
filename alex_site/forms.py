from django import forms
from django.conf import settings
from templated_mail.mail import BaseEmailMessage

from .models import Message

class MyEmailMessage(BaseEmailMessage):
    template_name = 'alex_site/feed-email.html'

    def get_context_data(self):
        context = super(MyEmailMessage, self).get_context_data()
        context['foo'] = 'bar'
        return context


class FeedForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'phone', 'comment']

    def send_email(self, request, context):
        MyEmailMessage(request, context).send(to=[settings.DEFAULT_FROM_EMAIL, 'haritonov.aka@gmail.com'])