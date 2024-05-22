from django.urls import path
from .views import create_applications, interaction_list, interaction_detail

app_name = 'client'

urlpatterns = [
    # path('contacts/', contact_list, name='contact_list'),
    # path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('create_applications/', create_applications, name='create_applications'),
    path('applications/', interaction_list, name='applications'),
    path('applications/<int:pk>/', interaction_detail, name='applications_detail'),
    # path('property/request/<int:property_id>/', property_request_create, name='property_request_create'),
    # path('feedback/', feedback_create, name='feedback_create'),
]
