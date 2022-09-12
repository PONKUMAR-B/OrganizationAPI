from django.urls import path
from employeeapp import views

urlpatterns = [
    path('',views.OrganizationView.as_view()),
    path('employees_details/',views.EmployeesView.as_view()),
    path('organization_additional/',views.OrganizationAdditional.as_view()),
    path('employees_additional/',views.EmployeesAdditional.as_view()),
]
