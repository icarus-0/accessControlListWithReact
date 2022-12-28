from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self,email,name,password=None,**extra_fields):
        if not email:
            raise ValueError("User must have an email")
        
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))
        
        return self.create_user(email,password,**extra_fields)




class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserAccountManager()

    def get_full_name(self):
        return self.name
    
    def __str__(self):
        return self.email


class RightGroups(models.Model):
    name = models.CharField(max_length=500,unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Rights(models.Model):
    name = models.CharField(max_length=500,unique=True)
    is_active = models.BooleanField(default=True)
    right_group = models.ForeignKey(RightGroups,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserRights(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    right =  models.ForeignKey(Rights,on_delete=models.CASCADE,null=True)
    group = models.ForeignKey(RightGroups,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.user)+" : "+str(self.right)+" : "+str(self.group)