from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(max_length=3000, blank=True, null=True)
    skills = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ContactInfo(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Contact info for {self.user_profile.user.username}"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255, default="Default School Name")
    degree = models.CharField(max_length=255)
    specialization = models.CharField(default="", max_length=255)
    yop = models.IntegerField(default=now().year)
    others = models.TextField(default="others if exist",blank=True,null=True)

    def __str__(self):
        return self.school_name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, default="Default Company Name")
    role = models.CharField(max_length=255)
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)
    description = models.TextField()

    def __str__(self):
        return self.company_name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    technologies_used = models.TextField(default="")
    published = models.DateField(default=now)
    description = models.TextField()
    url = models.URLField(default="http://example.com",blank=True,null=True)


    def __str__(self):
        return self.title


class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255,default="Default Issuer")
    date_issued = models.DateField(default=now)
    url = models.URLField(default="http://example.com",blank=True,null=True)
    description = models.TextField(default="")


    def __str__(self):
        return self.name

class LoginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)
