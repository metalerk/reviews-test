from django.urls import path
from .views import (
	GetReviewsView,
	PosttReviewsView,
)

app_name = 'reviews'

urlpatterns = [
	path('get_reviews/', GetReviewsView.as_view()),
	path('post_review/', PosttReviewsView.as_view()),
]