from django.db import models
# For Django admin
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username


# Create your models here.


# def my_decorator(functionWeAreWrapping):
#     def wrapper():
#         print("Something is happending before the dunction is called")
#         functionWeAreWrapping()
#         print("Sometging is happenidng afeter the function is called")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!!")

# say_hello()

