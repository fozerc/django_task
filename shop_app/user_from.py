from django.contrib.auth.forms import UserCreationForm, UsernameField
from shop_app.models import ShopUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)
        field_classes = {'username': UsernameField}
