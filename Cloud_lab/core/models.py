from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# algorithms database


class Algorithm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.TextField()

class UserAlgorithm(models.Model):
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()

class TestCase(models.Model):
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    input = models.TextField()
    expected_output = models.TextField()

class UserTestCase(models.Model):
    user_algorithm = models.ForeignKey(UserAlgorithm, on_delete=models.CASCADE)
    input = models.TextField()
    expected_output = models.TextField()