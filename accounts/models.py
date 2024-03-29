from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name 				= models.CharField(max_length=30, null=True)
    last_name 				= models.CharField(max_length=30,null=True)
    phone_number            = models.CharField(max_length=30,null=True)
    total_debt_amount       = models.CharField(max_length=50,null=True)
    zip_code                = models.CharField(max_length=30,null=True)
    state                   = models.CharField(max_length=30,null=True)
    age                     = models.IntegerField(null=True)


    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=False)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    hide_email				= models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class Admin_Emails(models.Model):
    email 					= models.EmailField()

    class Meta:
        verbose_name = ("Admin emails")
        verbose_name_plural = ("Admin emails")

    def __str__(self) :
        return str(self.email)

class User_offers(models.Model):
    name 					= models.CharField(max_length=30)
    url_text                = models.TextField()
    url                     = models.URLField()
    image                   = models.ImageField(upload_to='offers',default='default.png')

    class Meta:
        verbose_name = ("User offers")
        verbose_name_plural = ("User offers")

    def __str__(self):
        return str(self.name)