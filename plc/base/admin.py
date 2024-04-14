from django.contrib import admin

# Register your models here.
from .models import Compile
# Register your models here.
class CompileAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'text', 'starter', 'ext', 'input_command')
    search_fields = ['name', 'short_name', 'text', 'starter', 'ext', 'input_command']
admin.site.register(Compile, CompileAdmin)