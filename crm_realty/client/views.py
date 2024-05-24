from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Application, Feedback, Deal
from .forms import ApplicationCreateForm, ApplicationViewForm, FeedbackCreateForm
from employee.models import Employee


# @user_passes_test(lambda u: u.is_superuser)
def application_list(request):
    """
    Возвращает список всех заявок.
    """
    applications = Application.objects.all()
    paginator = Paginator(applications, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'client/application_list.html', {'page_obj': page_obj})


# @user_passes_test(lambda u: u.is_superuser)
def application_detail(request, pk):
    """
    Возвращает детали конкретного заявок.
    """
    interaction = get_object_or_404(Application, pk=pk)
    return render(request, 'client/application_detail.html', {'interaction': interaction})


def create_application(request):
    """
    Создает новую заявку и сохраняет ее в базе данных.
    """
    if request.method == 'POST':
        form = ApplicationCreateForm(request.POST)
        if form.is_valid():
            applications = form.save(commit=False)
            property = form.cleaned_data.get('property')
            employee = form.cleaned_data.get('responsible_employee')
            applications.property = property
            applications.responsible_employee = employee
            applications.save()
            return redirect('client:applications')
    else:
        form = ApplicationCreateForm()
    return render(request, 'client/application_create.html', {'form': form})


def feedback_create(request):
    """
    Создает новый отзыв и сохраняет его в базе данных.
    """
    if request.method == 'POST':
        form = FeedbackCreateForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            employee = form.cleaned_data.get('responsible_employee')
            client = form.cleaned_data.get('client')
            feedback.responsible_employee = employee
            feedback.client = client
            feedback.save()
            return redirect('client:applications')
    else:
        form = FeedbackCreateForm()
    return render(request, 'client/feedback_form.html', {'form': form})
