from django.db import models


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
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    responsible_employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='feedbacks')


class Deal(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('pending', 'В ожидании'),
        ('rejected', 'Отклонена клиентом'),
        ('closed', 'Закрыта')
    ]
    id = models.IntegerField(primary_key=True, auto_created=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='deals')
    responsible_employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, related_name='deals')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='deals')

    def __str__(self):
        return f'Deal number {self.id} for {self.application}'
