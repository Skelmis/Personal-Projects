from django.contrib import admin

from .models import TeamMember, Partner

admin.site.register((TeamMember, Partner))
