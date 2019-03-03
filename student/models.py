from django.db import models

class mregister(models.Model):
	name=models.CharField(max_length=25)
	roll_no=models.CharField(max_length=10)
	std=models.CharField(max_length=15)
	email=models.EmailField(max_length=50)
	phone=models.CharField(max_length=14)

	def __str__(self):
		return self.name