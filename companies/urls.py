from django.urls import path
from .views import (
	GetCompaniesView
)

app_name = 'companies'

urlpatterns = [
	path('list/', GetCompaniesView.as_view()),
]