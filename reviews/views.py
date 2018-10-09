from rest_framework.response import Response

from django.http import HttpRequest
from django.conf import settings

from .models import Review, Reviewer
from .serializers import ReviewSerializer, ReviewerSerializer
from utils.views import OpenAPIView, ProtectedAPIView


class GetReviews(ProtectedAPIView):
	"""
	Template View used as a landing-like page.
	"""
	
	def get(self, request, *args, **kwargs):
		""" Dummy landing page """
		
		reviews = Review.objects.all()
		response = ReviewSerializer(reviews)
		return Response(response.data)
