from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

app_name = 'users'

# URLs for token-based auth
urlpatterns = [
    path('auth/', obtain_jwt_token, name='user-auth'),
    path('refresh/', refresh_jwt_token, name='user-refresh'),
    path('verify/', verify_jwt_token, name='user-verify'),
]