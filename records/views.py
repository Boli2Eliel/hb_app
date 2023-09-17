from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.models import Account
from records.forms import AddProductForm, AddFormuleForm, AddUomForm
from records.models import Product, Formule, Uom


# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")


@login_required
def records(request):
    return render(request, "records/records.html")

@login_required()
def staff_list(request):
    staff = Account.objects.all()
    return render(request, "records/staff.html", {"staff": staff})


# =================================== PRODUCT ==========================================
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
        # self.object.created_by = self.request.user
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


@login_required
def update_product(request, pk):
    if request.user.is_authenticated:
        current_product = Product.objects.get(id=pk)
        form = AddProductForm(request.POST or None, instance=current_product)
        if form.is_valid():
            form.save()
            messages.success(request, "Le produit a été mis à jour avec succès!")
            return redirect('records:products_list')
        return render(request, 'records/update_product.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('records:home')


@login_required
def delete_product(request, pk):
    if request.user.is_authenticated:
        delete_it = Product.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Produit supprimé avec succès...")
        return redirect('records:products_list')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')


# =================================== END PRODUCT ==========================================

# =================================== FORMULES ==========================================

@login_required
def formules_list(request):
    formules = Formule.objects.all()
    return render(request, "records/formules_list.html", {"formules": formules})


class FormuleCreateView(LoginRequiredMixin, CreateView):
    model = Formule
    form_class = AddFormuleForm
    success_url = reverse_lazy('records:formules_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ajout formule'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.created_by = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


@login_required
def update_formule(request, pk):
    if request.user.is_authenticated:
        current_formule = Formule.objects.get(id=pk)
        form = AddFormuleForm(request.POST or None, instance=current_formule)
        if form.is_valid():
            form.save()
            messages.success(request, "Formule mis à jour avec succès!")
            return redirect('records:formules_list')
        return render(request, 'records/update_formule.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('records:home')


@login_required
def delete_formule(request, pk):
    if request.user.is_authenticated:
        delete_it = Formule.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Formule supprimé avec succès...")
        return redirect('records:formules_list')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

# =================================== FORMULES ==========================================


# =================================== UOM ==========================================

@login_required
def uom_list(request):
    uoms = Uom.objects.all()
    return render(request, "records/uoms_list.html", {"uoms": uoms})


class UomCreateView(LoginRequiredMixin, CreateView):
    model = Uom
    form_class = AddUomForm
    success_url = reverse_lazy('records:uoms_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ajout Unité'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.created_by = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


@login_required
def update_uom(request, pk):
    if request.user.is_authenticated:
        current_uom = Uom.objects.get(id=pk)
        form = AddUomForm(request.POST or None, instance=current_uom)
        if form.is_valid():
            form.save()
            messages.success(request, "Unité mise à jour avec succès!")
            return redirect('records:uoms_list')
        return render(request, 'records/update_uom.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('records:home')


@login_required
def delete_uom(request, pk):
    if request.user.is_authenticated:
        delete_it = Uom.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Unité supprimée avec succès...")
        return redirect('records:uoms_list')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

# =================================== UOM ==========================================