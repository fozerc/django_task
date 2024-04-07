from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView, UpdateView, ListView
from shop_app.models import ShopUser, Products, Purchase
from shop_app.forms import MyUserCreationForm, PurchaseForm


class MainTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'
    login_url = '/login/'


class AllProductsTemplate(UserPassesTestMixin, TemplateView):
    template_name = 'products.html'

    def test_func(self):
        return self.request.user.is_superuser


class AddProductTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'add_product.html'

    def test_func(self):
        return self.request.user.is_superuser


class ProductViewingReturns(LoginRequiredMixin, TemplateView):
    template_name = 'product_returns.html'


class UserLogin(LoginView):
    next_page = '/'
    template_name = 'login.html'


class UserLogout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class Register(CreateView):
    success_url = '/'
    queryset = ShopUser.objects.all()
    form_class = MyUserCreationForm
    template_name = 'register.html'


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    fields = ['name', 'product_description', 'price', 'quantity']
    template_name = 'add_product.html'
    success_url = reverse_lazy('add_product')


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Products
    fields = ['name', 'product_description', 'price', 'quantity']
    template_name = 'update_product.html'
    success_url = reverse_lazy('base.html')


class ProductsListView(ListView):
    model = Products
    paginate_by = 4
    template_name = 'products.html'
    extra_context = {'buy_form': PurchaseForm}


class PurchasesCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = PurchaseForm
    http_method_names = ['post']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['quantity'] = self.request.GET.get('quantity')
        kwargs['product'] = self.request.GET.get('product')
        return kwargs




