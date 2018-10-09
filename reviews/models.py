from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Reviewer
from companies.models import Company

from uuid import uuid4


class Review(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	company = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.IntegerFiedl(
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
