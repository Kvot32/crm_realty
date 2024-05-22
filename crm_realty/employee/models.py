# models.py
from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    CHOICES_ROLE = [
        ('sales_manager', 'Менеджер по продажам'),
        ('customer_service', 'Специалист по обслуживанию клиентов'),
        ('marketer', 'Маркетолог'),
        ('analyst', 'Аналитик')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    role = models.CharField(max_length=50, choices=CHOICES_ROLE)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
