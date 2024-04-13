from django.contrib import admin  # type: ignore

from user.models import Profile

admin.site.register(Profile)
