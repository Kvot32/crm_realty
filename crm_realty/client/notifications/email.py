from django.core.mail import send_mail


def send_email_to_client(client, deal):
    """Отправка уведомления клиенту по электронной почте"""
    email_host = 'smtp.example.com'
    email_port = 587
    email_host_user = 'ваш адрес лектронной почты'
    email_host_password = 'ваш пароль от почты'

    recipient_email = client.email

    subject = f"Сделка {deal.id} создана"
    message = f"Здравствуйте, {client.name},\n\nВаша сделка {deal.id} создана. Спасибо за сотрудничество."

    send_mail(
        subject=subject,
        message=message,
        from_email=email_host_user,
        recipient_list=[recipient_email],
        fail_silently=False,
        auth_user=email_host_user,
        auth_password=email_host_password,
        host=email_host,
        port=email_port
    )


def send_email_to_employee(employee, deal):
    """Отправка уведомления сотруднику по электронной почте"""
    email_host = 'smtp.example.com'
    email_port = 587
    email_host_user = 'ваш адрес лектронной почты'
    email_host_password = 'ваш пароль от почты'

    recipient_email = employee.email

    subject = f"Вам назначена сделка {deal.id}"
    message = f"Здравствуйте, {employee.user.username},\n\nВам назначена сделка {deal.id}. Пожалуйста, просмотрите и примите соответствующие меры."

    send_mail(
        subject=subject,
        message=message,
        from_email=email_host_user,
        recipient_list=[recipient_email],
        fail_silently=False,
        auth_user=email_host_user,
        auth_password=email_host_password,
        host=email_host,
        port=email_port
    )
