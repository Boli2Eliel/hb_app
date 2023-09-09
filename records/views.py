from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from records.forms import AddProductForm
from records.models import Product


# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")


@login_required
def products_list(request):
    products = Product.objects.all()
    return render(request, "records/products.html", {"products": products})

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = AddProductForm
    success_url = reverse_lazy('records:products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ajout produit'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.created_by = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

@login_required
def customer_product(request, pk):
    if request.user.is_authenticated:
        # Look Up Products
        customer_product = Product.objects.get(id=pk)
        return render(request, 'records/product_details.html', {'customer_product': customer_product})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')