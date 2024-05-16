from django.contrib import admin

from mailings.models import MailingSettings, Client, Message, Log


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'last_send', 'periodicity', 'status', 'is_active',)
    list_filter = ('owner', 'periodicity', 'status', 'is_active',)
    search_fields = ('owner', 'title',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'FIO', 'owner',)
    list_filter = ('owner',)
    search_fields = ('email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'owner',)
    list_filter = ('owner',)
    search_fields = ('title',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'owner', 'mailing_list', 'client',)
    list_filter = ('status', 'owner',)
