
from .models import Transaction, About1, Activity1, Activity2, Activity3, Message, AdminReply
from django.contrib import admin
from .models import Email
from django.core.mail import send_mail,  BadHeaderError
from django.contrib import admin


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo')  # نمایش فیلدهای مورد نظر در لیست


admin.site.register(Transaction, TransactionAdmin)


@admin.register(About1)
class About1Admin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Activity3)
class Activity3Admin(admin.ModelAdmin):
    list_display = ('description',)


# @admin.register(Activity1)
# class Activity1Admin(admin.ModelAdmin):
#     list_display = ('description',)


@admin.register(Activity2)
class Activity2Admin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')


class Activity1Admin(admin.ModelAdmin):
    list_display = ('get_description_preview',)
    fields = ('description',)

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return Activity1.objects.count() == 0

    def get_description_preview(self, obj):
        # نمایش پیش‌نمایش توضیحات در لیست داده‌ها
        return obj.description[:30]  # مثلا 30 کاراکتر اول

    get_description_preview.short_description = 'Description Preview'


admin.site.register(Activity1, Activity1Admin)


# class MessageAdmin(admin.ModelAdmin):
#     list_display = ['email', 'get_subject']
#
#     def get_subject(self, obj):
#         return obj.message  # از message به عنوان ویژگی برای نمایش استفاده شود
#
#     get_subject.short_description = 'Subject'  # یا هر نام دلخواه دیگری که مایلید
#     get_subject.admin_order_field = 'message'  # مرتب‌سازی بر اساس message
#
#
# admin.site.register(Message, MessageAdmin)

#
# class ReplyInline(admin.TabularInline):
#     model = AdminReply
#     extra = 1
#
#
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ['email', 'message']
#     inlines = [ReplyInline]


# admin.site.register(Message)
# # admin.site.register(AdminReply)
# from .models import Message, Reply

# @admin.register(AdminReply)
class ReplyInline(admin.TabularInline):  # یا admin.TabularInline
    model = AdminReply
    extra = 1  # تعداد فیلدهای خالی برای افزودن پاسخ جدید
    fields = ['reply_message', 'user_message','sent_to_user']  # فیلدهای فقط خواندنی در پنل ادمین


class MessageAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]


admin.site.register(Message, MessageAdmin)


class EmailAdmin(admin.ModelAdmin):
    actions = ['send_email_action']

    def send_email_action(self, request, queryset):
        for email in queryset:
            try:
                send_mail(
                    email.subject,
                    email.message,
                    email.from_email,
                    [email.to_email],
                    fail_silently=False,
                )
                email.sent = True
                email.save()
            except BadHeaderError as e:
                # اگر هدر ایمیل نامعتبر باشد، آن را چاپ کنید و ادامه دهید
                print(f"BadHeaderError: {e}")
                continue
            except Exception as e:
                # چاپ هر خطای دیگر
                print(f"Error: {e}")
                continue

        self.message_user(request, f'The selected emails have been sent.')

    send_email_action.short_description = "Send email to selected users"

admin.site.register(Email, EmailAdmin)