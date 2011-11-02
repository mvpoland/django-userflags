from django.contrib import admin

from userflags.models import Flag


class FlagAdmin(admin.ModelAdmin):
    raw_id_fields = ('users', )
    list_display = ('name',)
    search_fields = ['name', 'users__username']

admin.site.register(Flag, FlagAdmin)
