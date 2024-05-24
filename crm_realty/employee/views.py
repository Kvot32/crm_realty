from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import EmployeeUpdateForm, EmployeeCreationForm, EmployeeChangeForm, EmployeeRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Employee


User = get_user_model()

@login_required
def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    employee = get_object_or_404(Employee, user=user)
    if request.method == 'POST':
        user_form = EmployeeChangeForm(request.POST, instance=user)
        employee_form = EmployeeUpdateForm(request.POST, instance=employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            return redirect('employee:employee', pk=pk)
    else:
        user_form = EmployeeChangeForm(instance=user)
        employee_form = EmployeeUpdateForm(instance=employee)
    return render(request, 'employee/employee_profile_update.html', {'user_form': user_form, 'employee_form': employee_form})

def registration(request):
    if request.method == 'POST':
        user_form = EmployeeRegisterForm(request.POST)
        employee_form = EmployeeCreationForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('employee:login')
        else:
            return render(request, 'employee/register.html', {'user_form': user_form, 'employee_form': employee_form})
    else:
        user_form = EmployeeRegisterForm()
        employee_form = EmployeeCreationForm()
    return render(request, 'employee/register.html', {'user_form': user_form, 'employee_form': employee_form})


@login_required
def employee_profile(request, pk):
    """Отображает профиль сотрудника."""
    user = User.objects.get(pk=pk)
    employee = get_object_or_404(Employee, user=user)
    return render(request, 'employee/employee_profile.html', {'employee': employee, 'user':user})


class EmployerLogoutView(LogoutView):
    """Выход из системы."""
    next_page = reverse_lazy("employee:logout")
    http_method_names = ['get', 'post']

    def get_success_url(self):
        return reverse_lazy('employee:login')

"""Логин сотрудников"""
def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee:employee', pk=user.pk)
        else:
            return render(request, 'employee/login.html', {'error_message': 'Неверный логин или пароль'})
    else:
        return render(request, 'employee/login.html')

# @user_passes_test(lambda u: u.is_superuser)
def employees_list(request):
    """
    Возвращает список сотрудников.
    """
    employees = Employee.objects.all()
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'employee/employees_list.html', {'page_obj': page_obj})
