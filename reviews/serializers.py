from rest_framework import serializers
from .models import Review
from users.models import Reviewer
from companies.models import Company


class ReviewerSerializer(serializers.ModelSerializer):

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


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
        )


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = ReviewerSerializer()
    company = Company()

    class Meta:
        model = Review
        fields = '__all__'