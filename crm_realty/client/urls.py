from django.urls import path
from .views import create_application, application_list, application_detail, feedback_create, deal_create, deals_list, \
    deal_detail, deal_update

app_name = 'client'

urlpatterns = [
    path('deal_create/', deal_create, name='deal_create'),
    path('deals_list/', deals_list, name='deals_list'),
    path('deal_detail/<int:pk>/', deal_detail, name='deal_detail'),
    path('deal_update/<int:pk>/', deal_update, name='deal_update'),
    path('create_applications/', create_application, name='create_applications'),
    path('applications/', application_list, name='applications_list'),
    path('applications/<int:pk>/', application_detail, name='applications_detail'),
    path('feedback/', feedback_create, name='feedback_create'),
]
