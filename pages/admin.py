from django.contrib import admin
from . import models


@admin.register(models.HomeDescription)
class UserLinkAdmin(admin.ModelAdmin):
    list_display = ('description', 'link', 'pdf_file')

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return models.HomeDescription.objects.count() == 0


@admin.register(models.About1)
class About1Admin(admin.ModelAdmin):
    list_display = ('description', 'video_file', 'image_file')

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return models.About1.objects.count() == 0


class About2Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo')  # نمایش فیلدهای مورد نظر در لیست


admin.site.register(models.About2, About2Admin)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('description1', 'description2', 'description3',
                    'A', 'a', 'B', 'b', 'C', 'c',)

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return models.TokenDescription.objects.count() == 0


admin.site.register(models.TokenDescription, TokenAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('description', 'A', 'B', 'C', 'D',
                    'link', 'link_description', 'image_file')

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return models.Activity.objects.count() == 0


admin.site.register(models.Activity, ActivityAdmin)


class RoadmapDescriptionAdmin(admin.ModelAdmin):
    list_display = ('description',)

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return models.Roadmap1.objects.count() == 0


admin.site.register(models.Roadmap1, RoadmapDescriptionAdmin)


class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'description')


admin.site.register(models.Roadmap2, RoadmapAdmin)


class FooterDescriptionAdmin(admin.ModelAdmin):
    list_display = ('description1', 'description2', 'description3')

    def has_add_permission(self, request):
        # فقط اجازه افزودن یک داده داشته باشید
        return models.FooterDescription.objects.count() == 0


admin.site.register(models.FooterDescription, FooterDescriptionAdmin)


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('icon_class', 'profile_url')


admin.site.register(models.FooterLinks, FooterLinkAdmin)


class TimerAdmin(admin.ModelAdmin):
    list_display = ('date', )


admin.site.register(models.Timer, TimerAdmin)
