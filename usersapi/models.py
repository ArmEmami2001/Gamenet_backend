from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Subs(models.Model):
    subtime=models.DateField()
    # now=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.subtime}"
    
class Customer(models.Model):
    # name=models.CharField(max_length=100)
    # password=models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    subs=models.ForeignKey(Subs,on_delete=models.SET_NULL, null=True, blank=True)
    def sub(self):
        if timezone.now().date() < self.subs.subtime:
            subrem=(timezone.now().date())-(self.subs.subtime)
            return subrem
        else:
            return 0
    def __str__(self):
        # It's safer to check if self.user exists before accessing it
        if self.user:
            return f"{self.user.username} – {self.subs}"
        return f"Customer (No User) – {self.subs}"

class Worker(models.Model):
    name=models.CharField(max_length=100)
    worktime=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} – {self.worktime} "
    