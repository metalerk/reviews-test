from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer
from utils.views import ProtectedAPIView
from .models import Company


class GetCompaniesView(ProtectedAPIView):
	"""
	Get Reviews
	"""
	
	def get(self, request, *args, **kwargs):
		
		companies = Company.objects.filter()
		response = CompanySerializer(companies, many=True)
		return Response(response.data, status=status.HTTP_200_OK)
