from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Meal(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Rate(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = [["user", "meal"]]
        index_together = [["user", "meal"]]
