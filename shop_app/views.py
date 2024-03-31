from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from shop_app.models import ShopUser
from shop_app.user_from import MyUserCreationForm


class MainTemplateView(TemplateView):
    template_name = 'base.html'


class RegisterView(CreateView):
    from_class = MyUserCreationForm
    queryset = ShopUser.objects.all()
    template_name = 'register.html'


