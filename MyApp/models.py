from django.db import models

# Create your models here.

class BannerImage(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    banner_image = models.FileField(upload_to="banner/images", null=True, blank=True)


class Service(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    banner_image = models.FileField(upload_to="service/images", null=True, blank=True)


class Appointment(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    atime  = models.DateTimeField(null=True, blank=True)
    medium = models.CharField(max_length=20, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)


class ResumeUpload(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    Resume = models.FileField(upload_to="Resume", null=True, blank=True)


class TeamMember(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="Teammember", null=True, blank=True)

class Review(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    client_review = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="Client", blank=True, null=True)