from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images", blank=True, null=True)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.name