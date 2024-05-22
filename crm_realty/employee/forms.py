# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Employee


class EmployeeRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')


class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['role', 'phone']


class EmployeeChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['role', 'phone']

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']
#
#     def clean_password_confirm(self):
#         password = self.cleaned_data.get('password')
#         password_confirm = self.cleaned_data.get('password_confirm')
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError("Пароли не совпадают")
#         return password_confirm

# def save(self, commit=True):
#     user = super(UserRegistrationForm, self).save(commit=False)
#     user.set_password(self.cleaned_data['password'])
#     if commit:
#         user.save()
#     return user
