from rest_framework.response import Response
from rest_framework import status

from .models import Review
from users.models import Reviewer
from .serializers import ReviewSerializer, ReviewerSerializer
from utils.views import ProtectedAPIView
from utils.utils import get_or_none, get_ip_address
from companies.models import Company


class GetReviewsView(ProtectedAPIView):
	"""
	Get Reviews
	"""
	
	def get(self, request, *args, **kwargs):
		
		reviews = Review.objects.filter(reviewer=request.user)
		response = ReviewSerializer(reviews, many=True)
		return Response(response.data)


class PosttReviewsView(ProtectedAPIView):
	"""
	Get Reviews
	"""
	
	def post(self, request, *args, **kwargs):
		
		try:
			review = Review(
				company=get_or_none(model=Company,
									id=request.data.get('company', None)
				),
				reviewer=request.user,
				rating=request.data.get('rating'),
				title=request.data.get('title'),
				summary=request.data.get('summary'),
				is_employee=request.data.get('is_employee'),
				ip_address=get_ip_address(request=request)
			)
			review.save()
			serializer = ReviewSerializer(review)
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		except Exception as e:
			return Response({'error': e.__str__()},
				status=status.HTTP_400_BAD_REQUEST)
