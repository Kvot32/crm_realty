from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('cancelled', 'Отменена клиентом'),
        ('to_deal', 'На сделку'),
        ('pending', 'В ожидании')
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey("property.Property", on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    responsible_employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.client} - {self.property}'


class Feedback(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    comment = models.TextField()
    responsible_employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class Deal(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('pending', 'В ожидании'),
        ('rejected', 'Отклонена клиентом'),
        ('closed', 'Закрыта')
    ]
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    responsible_employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, related_name='deals_responsible')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Deal for {self.application}'
