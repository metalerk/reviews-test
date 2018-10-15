from rest_framework import serializers
from .models import Review
from users.models import Reviewer
from companies.serializers import CompanySerializer


class ReviewerSerializer(serializers.ModelSerializer):
    """ Serializer for model Reviewer """

    class Meta:
        model = Reviewer
        fields = (
        	'id',
        	'username',
        	'first_name',
        	'last_name',
        	'email',
            'is_active',
        )


class ReviewSerializer(serializers.ModelSerializer):
    """ Serializer for model Review """

    reviewer = ReviewerSerializer()
    company = CompanySerializer()

    class Meta:
        model = Review
        fields = '__all__'