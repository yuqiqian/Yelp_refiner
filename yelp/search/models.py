from django.db import models

# Create your models here.

class Business(models.Model):
	def __str__(self):
		return self.b_id
	b_id = models.CharField(max_length=200)
	b_name=models.CharField(max_length=200)
	b_zipcode=models.IntegerField(max_length=10)