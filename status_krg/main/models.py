from django.db import models

# Create your models here.
class Information(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)


class TypeActivity(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)


class Activity(models.Model):
    description = models.TextField(null=True)

    type_activity = models.ForeignKey(TypeActivity, on_delete=models.CASCADE)


class Repair(models.Model):
    photo = models.FileField(null=True, upload_to='uploads')
    title = models.TextField(null=True)
    description = models.TextField(null=True)


class Certificate(models.Model):
    photo = models.FileField(null=True, upload_to='uploads')


class Project(models.Model):
    photo = models.FileField(null=True, upload_to='uploads')
    title = models.TextField(null=True)
    description = models.TextField(null=True)


class FeedBack(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    message = models.TextField(null=True)


class Link(models.Model):
    whatsapp_link = models.TextField(null=True)
    instagram_link = models.TextField(null=True)
    facebook_link = models.TextField(null=True)
    vk_link = models.TextField(null=True)
    