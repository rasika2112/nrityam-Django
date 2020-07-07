from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator


class Feedbacks(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phoneNo= models.CharField(max_length=12)
    feedback=models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
