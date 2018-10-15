from django.urls import path
from .views import (
	GetReviewsView,
	PosttReviewsView,
	RetrieveReviewsView,
)

app_name = 'reviews'

urlpatterns = [
	path('list/', GetReviewsView.as_view()),
	path('list/<int:page>', GetReviewsView.as_view()),
	path('retrieve/', RetrieveReviewsView.as_view()),
	path('create/', PosttReviewsView.as_view()),
]