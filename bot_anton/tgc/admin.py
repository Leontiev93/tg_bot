from django.contrib import admin

from .forms import ProfileForm
from .models import Profile, Massage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')
