from profiles.models import ProfileCategory

from django.contrib import admin


@admin.register(ProfileCategory)
class ProfileCategoryAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "color", "updated_at")
