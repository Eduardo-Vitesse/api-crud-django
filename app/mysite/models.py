from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.fullname

# Create / Insert / Add - POST
# Retrieve / Fetch - GET
# Updata / Edit - PUT
# Delete / Remove - DELETE
