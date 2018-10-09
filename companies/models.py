from django.db import models
from uuid import uuid4


class Company(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=150)
	submission_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		db_table = 'companies'
		verbose_name_plural = 'Companies'
		ordering = ['-submission_date']
