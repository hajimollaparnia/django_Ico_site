from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class HomeDescription(models.Model):
    description = RichTextField()
    link = models.URLField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.description


class About1(models.Model):
    description = RichTextField()
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)


class About2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.CharField(max_length=50, blank=True)  # خالی بدون مقدار پیش‌فرض

    def __str__(self):
        return self.title


class TokenDescription(models.Model):
    A = models.CharField(max_length=30, default='0')
    a = models.CharField(max_length=30, default='0')

    B = models.TextField()
    b = models.CharField(max_length=30, default='0')

    C = models.CharField(max_length=30, default='0')
    c = models.TextField(null=True, blank=True)

    D = models.CharField(max_length=30, default='0')
    d = models.TextField(null=True, blank=True)

    description1 = RichTextField(null=True, blank=True)
    description2 = RichTextField(null=True, blank=True)
    description3 = RichTextField(null=True, blank=True)

    join_us_link = models.URLField(null=True, blank=True)
    buy_link = models.URLField(null=True, blank=True)


class Activity(models.Model):
    description = RichTextField()

    A = RichTextField(null=True, blank=True)
    B = RichTextField(null=True, blank=True)
    C = RichTextField(null=True, blank=True)
    D = RichTextField(null=True, blank=True)

    link = models.URLField(null=True, blank=True)
    link_description = models.TextField(null=True, blank=True)

    image_file = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.description


class Link(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link


class Roadmap1(models.Model):
    description = RichTextField()


class Roadmap2(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return f"{self.title} - {self.date}"


class FooterDescription(models.Model):
    description1 = RichTextField(null=True, blank=True)
    description2 = RichTextField(null=True, blank=True)
    description3 = RichTextField(null=True, blank=True)


class FooterLinks(models.Model):

    icon_class = models.CharField(max_length=50, null=True, blank=True)
    profile_url = models.URLField(null=True, blank=True)


class Timer(models.Model):
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)


class SiteVisit(models.Model):
    admin_only_count = models.IntegerField(default=0)

