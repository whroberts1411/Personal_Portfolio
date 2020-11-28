from django.contrib import admin
from .models import Blog

class PageAdmin(admin.ModelAdmin):
    """ This adds an additional field to the admin display, sorts the 
        output and allows searching on the specified field.  """

    list_display = ('title', 'date')
    ordering = ('-date', 'title')       # latest date/time first!
    search_fields = ('title',)

admin.site.register(Blog, PageAdmin)
