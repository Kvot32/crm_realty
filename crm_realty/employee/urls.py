from django.urls import path

from .views import registration, employee_profile, employee_login, profile_update, EmployerLogoutView

app_name = 'employee'

urlpatterns = [
    path('login/', employee_login, name='login'),
    path('register/', registration, name='register'),
    path('employee/<int:pk>/', employee_profile, name='employee'),
    path('employee_update/<int:pk>/', profile_update, name='employee_update'),
    path('logout/', EmployerLogoutView.as_view(), name='logout'),


]
