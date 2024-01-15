from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


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
    A = models.CharField(max_length=10, default='0')
    a = models.CharField(max_length=10, default='0')

    B = models.TextField()
    b = models.CharField(max_length=10, default='0')

    C = models.CharField(max_length=10, default='0')
    c = models.TextField(null=True, blank=True)

    D = models.CharField(max_length=10, default='0')
    d = models.TextField(null=True, blank=True)

    description1 = RichTextField(null=True, blank=True)
    description2 = RichTextField(null=True, blank=True)
    description3 = RichTextField(null=True, blank=True)

    days = models.CharField(max_length=10, default='0')
    hours = models.CharField(max_length=10, default='0')
    minutes = models.CharField(max_length=10, default='0')
    seconds = models.CharField(max_length=10, default='0')

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
    description1 = RichTextField()
    description2 = RichTextField()


class FooterLinks(models.Model):
    link = models.URLField(null=True, blank=True)
    link_description = models.TextField(null=True, blank=True)


class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    to_email = models.EmailField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject




#
# class Message(models.Model):
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(default='2024-01-01 00:00:00')
#
#     def __str__(self):
#         return self.email
