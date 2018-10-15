from django.contrib import admin
from .models import Reviewer
from .forms import ReviewerCreationForm, ReviewerChangeForm


@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
	""" Admin handler for Reviewer model """

	add_form = ReviewerCreationForm
	form = ReviewerChangeForm
	model = Reviewer