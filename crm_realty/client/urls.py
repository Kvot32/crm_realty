from django.urls import path
from .views import create_application, application_list , application_detail, feedback_create

app_name = 'client'

urlpatterns = [
    # path('contacts/', contact_list, name='contact_list'),
    # path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('create_applications/', create_application, name='create_applications'),
    path('applications/', application_list, name='applications'),
    path('applications/<int:pk>/', application_detail, name='applications_detail'),
    # path('property/request/<int:property_id>/', property_request_create, name='property_request_create'),
    path('feedback/', feedback_create, name='feedback_create'),
]
