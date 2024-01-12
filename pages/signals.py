# # signals.py
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import AdminReply
#
#
# @receiver(post_save, sender=AdminReply)
# def send_email_to_user(sender, instance, **kwargs):
#     if instance.sent_to_user:
#         send_mail(
#             'پاسخ به پیام شما',
#             f'سلام {instance.message.email}\n\nپیام شما دریافت شده است. \n\nپاسخ مدیر: {instance.reply_text}',
#             'hajimollaparnia7676@gmail.com',  # ایمیلی که از آن ارسال می‌شود
#             [instance.message.email],
#             fail_silently=False,
#         )
