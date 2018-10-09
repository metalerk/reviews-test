from django.urls import path
from .views import (
	GetCompaniesView
)

app_name = 'companies'

urlpatterns = [
	path('get_companies/', GetCompaniesView.as_view()),
]