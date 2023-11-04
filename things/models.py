from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, blank = False, unique=True)
    description = models.CharField(max_length=120, blank = True, unique=False)
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], unique=False)

#
