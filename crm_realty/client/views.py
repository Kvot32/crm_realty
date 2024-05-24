from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Application, Deal
from .forms import ApplicationCreateForm, FeedbackCreateForm, DealCreateForm, DealUpdateForm
from notifications.email import send_email_to_client, send_email_to_employee


# @user_passes_test(lambda u: u.is_superuser)
def application_list(request):
    """
    Возвращает список всех заявок.
    """
    applications = Application.objects.all()
    paginator = Paginator(applications, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'client/applications_list.html', {'page_obj': page_obj})


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
            client = form.cleaned_data.get('client')
            applications.property = property
            applications.client = client
            applications.responsible_employee = employee
            applications.save()

            return redirect('client:applications_list')


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
            return redirect('client:applications_list')
    else:
        form = FeedbackCreateForm()
    return render(request, 'client/feedback_form.html', {'form': form})


def deal_create(request):
    """Создание сделки"""
    if request.method == "POST":
        form = DealCreateForm(request.POST, request.FILES)
        if form.is_valid():
            deal = form.save(commit=False)
            application = form.cleaned_data.get("application")
            employee = form.cleaned_data.get('responsible_employee')
            client = form.cleaned_data.get('client')
            deal.application = application
            deal.responsible_employee = employee
            deal.client = client
            deal.save()

            send_email_to_client(client, deal)
            send_email_to_employee(employee, deal)

            return redirect('client:deals_list')
        else:
            return render(request, 'client/deal_create.html', {"form": form})
    else:
        form = DealCreateForm()
    return render(request, 'client/deal_create.html', {"form": form})


def deals_list(request):
    """Спиисок сделок"""
    deals = Deal.objects.all().order_by('-created_at', 'id')
    paginator = Paginator(deals, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'client/deals_list.html', {'page_obj': page_obj})


def deal_detail(request, pk):
    """Детальный просмотр сделки"""
    deal = get_object_or_404(Deal, pk=pk)
    return render(request, 'client/deal_detail.html', {"deal": deal})


def deal_update(request, pk):
    """Обновление/изменение сделки"""
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        form = DealUpdateForm(request.POST, instance=deal)
        if form.is_valid():
            deal = form.save(commit=False)
            employee = form.cleaned_data.get('responsible_employee')
            deal.responsible_employee = employee
            deal.save()
            return redirect('client:deals_list')
        else:
            return render(request, 'client/deal_update.html', {'form': form})

    else:
        form = DealUpdateForm()
    return render(request, 'client/deal_update.html', {'form': form})
