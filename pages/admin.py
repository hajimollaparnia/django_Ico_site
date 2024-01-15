

from . import models
from django.contrib import admin


@admin.register(models.HomeDescription)
class UserLinkAdmin(admin.ModelAdmin):
    list_display = ('description', 'link', 'pdf_file')

    # def has_add_permission(self, request):
    #     # فقط اجازه افزودن یک داده داشته باشید
    #     return Activity1.objects.count() == 0


@admin.register(models.About1)
class About1Admin(admin.ModelAdmin):
    list_display = ('description', 'video_file', 'image_file')


class About2Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo')  # نمایش فیلدهای مورد نظر در لیست


admin.site.register(models.About2, About2Admin)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('description1', 'description2', 'description3',
                    'A', 'a', 'B', 'b', 'C', 'c', 'days',
                    'hours', 'minutes', 'seconds')


admin.site.register(models.TokenDescription, TokenAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('description', 'A', 'B', 'C', 'D',
                    'link', 'link_description', 'image_file')


admin.site.register(models.Activity, ActivityAdmin)


class RoadmapDescriptionAdmin(admin.ModelAdmin):
    list_display = ('description',)


admin.site.register(models.Roadmap1, RoadmapDescriptionAdmin)


class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'description')


admin.site.register(models.Roadmap2, RoadmapAdmin)


class FooterDescriptionAdmin(admin.ModelAdmin):
    list_display = ('description1', 'description2')


admin.site.register(models.FooterDescription, FooterDescriptionAdmin)


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'link_description')


admin.site.register(models.FooterLinks, FooterLinkAdmin)


# class TimeraAdmin(admin.ModelAdmin):
#     form = forms.TimerAdminForm
#     list_display = ('start_date', 'end_date')
#
#
# admin.site.register(models.Timer, TimeraAdmin)
#
#
# class TAdmin(admin.ModelAdmin):
#     list_display = ('event_date', 'name')
#
#
# admin.site.register(models.Event, TAdmin)

#
# @admin.register(Activity3)
# class Activity3Admin(admin.ModelAdmin):
#     list_display = ('description',)
#
#
# @admin.register(Activity2)
# class Activity2Admin(admin.ModelAdmin):
#     list_display = ('title', 'date', 'description')
#
#
# class Activity1Admin(admin.ModelAdmin):
#     list_display = ('get_description_preview',)
#     fields = ('description',)
#
#     def has_add_permission(self, request):
#         # فقط اجازه افزودن یک داده داشته باشید
#         return Activity1.objects.count() == 0
#
#     def get_description_preview(self, obj):
#         # نمایش پیش‌نمایش توضیحات در لیست داده‌ها
#         return obj.description[:30]  # مثلا 30 کاراکتر اول
#
#     get_description_preview.short_description = 'Description Preview'
#
#
# admin.site.register(Activity1, Activity1Admin)
#
#
# class ReplyInline(admin.TabularInline):  # یا admin.TabularInline
#     model = AdminReply
#     extra = 1  # تعداد فیلدهای خالی برای افزودن پاسخ جدید
#     fields = ['reply_message', 'user_message', 'sent_to_user']  # فیلدهای فقط خواندنی در پنل ادمین
#
#
# class MessageAdmin(admin.ModelAdmin):
#     inlines = [ReplyInline]
#
#
# admin.site.register(Message, MessageAdmin)
#
#
# class EmailAdmin(admin.ModelAdmin):
#     actions = ['send_email_action']
#
#     def send_email_action(self, request, queryset):
#         for email in queryset:
#             try:
#                 send_mail(
#                     email.subject,
#                     email.message,
#                     email.from_email,
#                     [email.to_email],
#                     fail_silently=False,
#                 )
#                 email.sent = True
#                 email.save()
#             except BadHeaderError as e:
#                 # اگر هدر ایمیل نامعتبر باشد، آن را چاپ کنید و ادامه دهید
#                 print(f"BadHeaderError: {e}")
#                 continue
#             except Exception as e:
#                 # چاپ هر خطای دیگر
#                 print(f"Error: {e}")
#                 continue
#
#         self.message_user(request, f'The selected emails have been sent.')
#
#     send_email_action.short_description = "Send email to selected users"
#
#
# admin.site.register(Email, EmailAdmin)
#
#
# @admin.register(Token)
# class TokenAdmin(admin.ModelAdmin):
#     list_display = ('name', 'symbol', 'total_supply')
#
#
# @admin.register(ICO)
# class ICOAdmin(admin.ModelAdmin):
#     list_display = ('token', 'start_date', 'end_date', 'hard_cap', 'soft_cap')
#
#
# @admin.register(TokenPurchase)
# class TokenPurchaseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'token', 'quantity', 'price', 'date_purchased')
#
#
# @admin.register(UserWallet)
# class UserWalletAdmin(admin.ModelAdmin):
#     list_display = ('user', 'balance')
