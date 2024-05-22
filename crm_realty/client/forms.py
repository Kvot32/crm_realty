from django import forms
from .models import Client, Application, Feedback


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'notes']


class ApplicationCreatedForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['description', 'client', 'property', 'status', 'responsible_employee']


class ApplicationViewForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['description', 'client', 'property', 'status', 'responsible_employee']


class FeedbackCreatedForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['application', 'comment', 'responsible_employee']

