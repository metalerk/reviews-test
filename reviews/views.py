from rest_framework.response import Response

from django.http import HttpRequest
from django.conf import settings

from .models import Review
from users.models import Reviewer
from .serializers import ReviewSerializer, ReviewerSerializer
from utils.views import OpenAPIView, ProtectedAPIView


class GetReviewsView(ProtectedAPIView):
	"""
	Get Reviews
	"""
	
	def get(self, request, *args, **kwargs):
		
		reviews = Review.objects.all()
		response = ReviewSerializer(reviews, many=True)
		return Response(response.data)
