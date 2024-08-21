from django.contrib import admin
from .forms import CustomerUserCreationForm, CustomerUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser
# Register your models here.


class CustomerUserAdmin(UserAdmin):
    form = CustomerUserChangeForm
    add_form = CustomerUserCreationForm
    model = CustomerUser
    list_display = ['email', 'username', 'is_staff', 'age']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {'fields': ('age',)}),)


admin.site.register(CustomerUser, CustomerUserAdmin)
