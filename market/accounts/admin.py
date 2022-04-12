from django.contrib import admin

# Register your models here.
from accounts.models import Account, Key, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("job_id", "state", "type", "result", "transaction_id")


admin.site.register(Account)
admin.site.register(Key)
