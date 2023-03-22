# from django.db import models
# from django.contrib.auth.models import User, Group, AbstractUser
# import uuid

# # Create your models here.

# class Profile(AbstractUser):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     # profile = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     # user = models.OneToOneField(User, default=uuid.uuid4, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=500, blank=True, null=True)

#     def __str__(self):
#         return str(self.user.username)