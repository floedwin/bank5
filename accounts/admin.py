from django.contrib import admin

from .models import Registercustomer,Registercustomertranscations,CustomerBankaccount
admin.site.register(Registercustomer)
admin.site.register(Registercustomertranscations)
admin.site.register(CustomerBankaccount)
admin.site.site_header ='Administration'
