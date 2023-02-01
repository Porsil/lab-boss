from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


AVAILABLE_STATUS = (("Active", "Active"), ("Inactive", "Inactive"))
WORKLOAD_STATUS = (("To Do", "To Do"), ("Completed", "Completed"))


class Analyst(models.Model):
    name = models.CharField(max_length=30, unique=True)
    status = models.TextField(choices=AVAILABLE_STATUS, default="Active")

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=30, unique=True)
    status = models.TextField(choices=AVAILABLE_STATUS, default="Active")

    def __str__(self):
        return self.name


class Workload(models.Model):
    test_date = models.DateField()
    analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE,
                                limit_choices_to={'status': 'Active'},)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,
                             limit_choices_to={'status': 'Active'},)
    comment = models.CharField(max_length=50, blank=True)
    status = models.TextField(choices=WORKLOAD_STATUS, default="To Do")

    class Meta:
        ordering = ['test_date']

    def __str__(self):
        return f"{self.analyst} to test {self.test} on {self.test_date}"
