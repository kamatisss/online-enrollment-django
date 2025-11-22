from django.urls import path
from . import views

urlpatterns = [
    path('enrol/', views.enroll_user, name='enroll_user'),
    path("enroll/", views.EnrollmentWizard.as_view(), name="enroll"),
    

]