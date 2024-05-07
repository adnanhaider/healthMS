from django.db import models

class HealthMeter(models.Model):
    age = models.IntegerField(max_length=2)
    def __str__(self):
        return self.age
    
    
class Result(models.Model):
    healthmeter = models.ForeignKey(HealthMeter, on_delete=models.CASCADE)
    result = models.CharField(max_length=200)
    def __str__(self):
        return self.result

