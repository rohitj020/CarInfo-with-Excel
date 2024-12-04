from django.db import models

# Create your models here.
class cars(models.Model):
    id = models.AutoField(primary_key=True)
    City = models.CharField(max_length=50)
    CarName = models.CharField(max_length=50)
    CarPrice = models.IntegerField()
    Company = models.CharField(max_length=50)

    class Meta:
        db_table = 'Cars Data'

