from django.contrib import admin

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass

class BillingAdmin(admin.ModelAdmin):
    pass

from user_data.models import Customer, Billing
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Billing, BillingAdmin)