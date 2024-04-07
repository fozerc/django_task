from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm

from shop_app.models import ShopUser, Purchase
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)
        field_classes = {'username': UsernameField}


class PurchaseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.user = kwargs.pop('user')

    class Meta:
        model = Purchase
        fields = ('quantity',)

    def clean(self):
        self.user = ShopUser.objects.get(username=self.cleaned_data['username'])
        

