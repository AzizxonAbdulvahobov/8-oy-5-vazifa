from django.db import models

# Create your models here.

class Teachers(models.Model):
    ful_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    expirience = models.IntegerField()
  
    def __str__(self):
        return self.ful_name



class Courses(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    davomiyligi = models.IntegerField()
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Students(models.Model):
    cource = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    ful_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    parent_phone = models.CharField(max_length=13)
    tg_link = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.ful_name
