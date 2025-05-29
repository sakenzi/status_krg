from django.contrib import admin
from .models import *
# Register your models here.

class InformationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address', 'description')


# class TypeActivityAdmin(admin.ModelAdmin):
#     list_display = ('name')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('description', 'type_activity')


class RepairAdmin(admin.ModelAdmin):
    list_display = ('photo', 'title', 'description')


# class CertificateAdmin(admin.ModelAdmin):
#     list_display = ('photo')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('photo', 'title', 'description')


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'title', 'message')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('whatsapp_link', 'instagram_link', 'facebook_link', 'vk_link')


admin.site.register(Information, InformationAdmin)
admin.site.register(TypeActivity)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(Certificate)
admin.site.register(Project, ProjectAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Link, LinkAdmin)