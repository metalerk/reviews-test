from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'rating', 'reviewer', 'ip_address', 'submission_date')