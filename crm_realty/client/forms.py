from django import forms
from .models import Client, Application, Feedback, Deal


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'notes']


class ApplicationCreateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['description', 'client', 'property', 'status', 'responsible_employee']


class ApplicationViewForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['description', 'client', 'property', 'status', 'responsible_employee']


class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['application', 'comment', 'responsible_employee', 'client']


class DealCreateForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['application', 'responsible_employee', 'status', 'documents', 'description', 'client']


class DealDetailForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['application', 'responsible_employee', 'status', 'documents', 'description', 'client']


class DealUpdateForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['application', 'responsible_employee', 'status', 'documents', 'description']
