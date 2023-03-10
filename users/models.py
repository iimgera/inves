# from django.db import models
# from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)



# class UserManager(BaseUserManager):
#     def create_superuser(self, email, password=None, **kwargs):
#         user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email
