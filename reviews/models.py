from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Reviewer
from companies.models import Company

from uuid import uuid4


class Review(models.Model):
	""" Review entity. """

	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company1')
	reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='reviewer1')
	rating = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(5), MinValueValidator(1)]
	)
	title = models.CharField(max_length=64)
	summary = models.TextField(max_length=10000)
	is_employee = models.BooleanField()
	ip_address = models.GenericIPAddressField(unpack_ipv4=True)
	submission_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		db_table = 'reviews'
		verbose_name_plural = 'Reviews'
		ordering = ['-submission_date']
