# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


# Local Django
from salyangoz.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'time', 'counter')
    list_display_link = ('title',)
    search_field = ('title', 'content')


admin.site.register(User, UserAdmin)
