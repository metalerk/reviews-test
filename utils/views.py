from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView


class OpenAPIView(APIView):
	"""
	This class sets the default permissions to open resources.
	"""

	permission_classes = (AllowAny,)


class ProtectedAPIView(APIView):
	"""
	This class sets the default permissions to protected resources.
	"""

	authentication_classes = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)


class AdminAPIView(ProtectedAPIView):
	"""
	This class sets the default permissions to open resources.
	"""

	permission_classes = (IsAuthenticated, IsAdminUser,)