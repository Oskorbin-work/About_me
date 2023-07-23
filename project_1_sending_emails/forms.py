from django import forms
from .models import EmailTemplate, EmailRecipient
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser


class EmailForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EmailForm, self).__init__(*args, **kwargs)
        if self.user != AnonymousUser():
            self.fields['emails_to'] = forms.ModelMultipleChoiceField(
                queryset=EmailRecipient.objects.all().filter(user_owner=self.user))
            self.fields['template'] = forms.ModelChoiceField(
                queryset=EmailTemplate.objects.all().filter(user_owner=self.user))

    subject = forms.CharField(max_length=70)


class NewEmailRecipientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewEmailRecipientForm, self).__init__(*args, **kwargs)
        self.fields['user_owner'] = forms.ModelChoiceField(
            queryset=User.objects.all(), initial=self.user, disabled=True)

    class Meta:
        model = EmailRecipient
        fields = '__all__'


class NewEmailTemplateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewEmailTemplateForm, self).__init__(*args, **kwargs)
        self.fields['user_owner'] = forms.ModelChoiceField(queryset=User.objects.all(), initial=self.user, disabled=True)

    class Meta:
        model = EmailTemplate
        fields = '__all__'