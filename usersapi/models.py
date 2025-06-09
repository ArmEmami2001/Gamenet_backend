from django.db import models
from django.utils import timezone

class Subs(models.Model):
    subtime=models.DateField()
    # now=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.subtime}"
    
class Customer(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    subs=models.ForeignKey(Subs,on_delete=models.SET_NULL, null=True, blank=True)
    def sub(self):
        if timezone.now().date() < self.subs.subtime:
            subrem=(timezone.now().date())-(self.subs.subtime)
            return subrem
        else:
            return 0
    def __str__(self):
        return f"{self.name} – {self.subs} "

class Worker(models.Model):
    name=models.CharField(max_length=100)
    worktime=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} – {self.worktime} "
    