from django.urls import path
from .views import (
	GetReviewsView,
)

app_name = 'reviews'

urlpatterns = [
	path('get_reviews/', GetReviewsView.as_view()),
]