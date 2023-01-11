from django.contrib import admin

from Access.models import User, Permission, UserAccessMapping, Role, AccessV2

admin.site.register(Permission)
admin.site.register(UserAccessMapping)
admin.site.register(Role)
admin.site.register(AccessV2)
