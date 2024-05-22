from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Application, Feedback, Deal
from .forms import ApplicationCreatedForm, ApplicationViewForm,  FeedbackCreatedForm
from employee.models import Employee


# @user_passes_test(lambda u: u.is_superuser)
def interaction_list(request):
    """
    Возвращает список всех заявок.
    """
    applications = Application.objects.select_related('employee', 'responsible_employee').all()
    paginator = Paginator(applications, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'client/application_list.html', {'applications': applications, 'page_obj': page_obj})


# @user_passes_test(lambda u: u.is_superuser)
def interaction_detail(request, pk):
    """
    Возвращает детали конкретного заявок.
    """
    interaction = get_object_or_404(Application, pk=pk)
    return render(request, 'client/application_detail.html', {'interaction': interaction})



#
def create_applications(request):
    """
    Создает новую заявку и сохраняет ее в базе данных.
    """
    if request.method == 'POST':
        form = ApplicationCreatedForm(request.POST)
        if form.is_valid():
            applications = form.save(commit=False)
            property = form.cleaned_data.get('property')
            employee = form.cleaned_data.get('responsible_employee')
            applications.property = property
            applications.responsible_employee = employee
            applications.save()
            return redirect('client:applications')
    else:
        form = ApplicationCreatedForm()
    return render(request, 'client/application_create.html', {'form': form})

#
# @user_passes_test(lambda u: u.is_superuser)
# def property_request_create(request, property_id):
#     """
#     Создает новый запрос на просмотр объекта недвижимости и сохраняет его в базе данных.
#     """
#     if request.method == 'POST':
#         form = PropertyRequestForm(request.POST)
#         if form.is_valid():
#             property_request = form.save(commit=False)
#             property_request.user = request.user
#             property_request.property_id = property_id
#             property_request.save()
#             return redirect('property:property_detail', pk=property_id)
#     else:
#         form = PropertyRequestForm()
#     return render(request, 'client/property_request_form.html', {'form': form})
#
#
# def feedback_create(request):
#     """
#     Создает новый отзыв и сохраняет его в базе данных.
#     """
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             feedback = form.save(commit=False)
#             feedback.user = request.user
#             feedback.save()
#             return redirect('client:interactions')
#     else:
#         form = FeedbackForm()
#     return render(request, 'client/feedback_form.html', {'form': form})
