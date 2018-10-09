from rest_framework import serializers
from .models import Review, Reviewer


class ReviewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviewer
        fields = (
        	'id',
        	'username',
        	'first_name',
        	'last_name',
        	'email',
        	'created',
        )


class ReviewSerializer(serializers.ModelSerializer):
	reviewer = Reviewer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'