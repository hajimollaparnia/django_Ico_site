from django import forms
from .models import Message
from django import forms
from .models import Message, AdminReply
from django import forms
from .models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'message', 'from_email', 'to_email']


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['email', 'message']


class AdminReplyForm(forms.ModelForm):
    class Meta:
        model = AdminReply
        fields = ['reply_message']

