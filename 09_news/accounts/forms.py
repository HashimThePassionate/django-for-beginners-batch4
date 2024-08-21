from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = UserChangeForm.Meta.fields
