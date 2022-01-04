from django.contrib import admin

from worc.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name", "email"]
    list_filter = ["is_staff", "is_superuser"]
