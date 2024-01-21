from .models import Email
from django import forms


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'message', 'from_email', 'to_email']


# class UserMessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['email', 'message']



