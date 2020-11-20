from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,*args, **kwargs):
        if not email:
            raise ValueError("Email required to create user")
        email = self.normalize_email(email)
        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.save(using=self.db)
        return user_obj
    
    def create_staff(self,email,password=None,*args, **kwargs):
        user_obj = self.create_user(email,password)
        user_obj.staff = True
        user_obj.save(using=self.db)
        return user_obj

    def create_superuser(self,email,password=None,*args, **kwargs):
        user_obj = self.create_user(email,password)
        user_obj.staff = True
        user_obj.admin = True
        user_obj.save(using=self.db)
        return user_obj


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """This class override the djnago base user"""
    email               = models.EmailField(max_length=200,unique=True)
    name                = models.CharField(max_length=150,null=True,blank=True)
    active              = models.BooleanField(default=True)
    staff               = models.BooleanField(default=False)
    admin               = models.BooleanField(default=False)
    updated_at          = models.DateTimeField(auto_now=True)
    created_at          = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS= []

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,object=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
