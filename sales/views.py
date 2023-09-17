from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.models import Account
from sales.forms import AddSalesPointForm
from sales.models import SalesPoint


# =================================== SALES_POINTS ==========================================

@login_required
def sales_points_list(request):
    sales_points = SalesPoint.objects.all()
    return render(request, "sales/sales_list.html", {"sales_points": sales_points})


class SalesPointsCreateView(LoginRequiredMixin, CreateView):
    model = SalesPoint
    form_class = AddSalesPointForm
    success_url = reverse_lazy('sales:sales_points_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ajout Point de vente'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.created_by = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


@login_required
def update_sales_point(request, pk):
    if request.user.is_authenticated:
        current_sales_point = SalesPoint.objects.get(id=pk)
        form = AddSalesPointForm(request.POST or None, instance=current_sales_point)
        if form.is_valid():
            form.save()
            messages.success(request, "Point de vente mis à jour avec succès!")
            return redirect('sales:sales_points_list')
        return render(request, 'sales/update_sales_point.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('records:home')


@login_required
def delete_sales_point(request, pk):
    if request.user.is_authenticated:
        delete_it = SalesPoint.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Point de vente supprimé avec succès...")
        return redirect('sales:sales_points_list')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

# =================================== SALES_POINTS ==========================================