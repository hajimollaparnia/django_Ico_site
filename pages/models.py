from django.db import models
from ckeditor.fields import RichTextField


class About1(models.Model):
    description = RichTextField()


class Transaction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.CharField(max_length=50, blank=True)  # خالی بدون مقدار پیش‌فرض

    def __str__(self):
        return self.title


class Activity1(models.Model):
    description = RichTextField()


class Activity2(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.date}"


class Activity3(models.Model):
    description = RichTextField()


class Message(models.Model):

    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default='2024-01-01 00:00:00')

    def __str__(self):
        return self.email


class AdminReply(models.Model):
    user_message = models.ForeignKey(Message, related_name='replies', on_delete=models.CASCADE)
    reply_message = models.TextField()
    created_at = models.DateTimeField(default='2024-01-01 00:00:00')
    sent_to_user = models.BooleanField(default=False)

    def __str__(self):
        return f"Reply to {self.user_message.email}"


class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    to_email = models.EmailField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

