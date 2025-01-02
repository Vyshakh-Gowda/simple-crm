# crm/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer, Deal
from .forms import CustomerForm, DealForm

@login_required
def dashboard(request):
    customers = Customer.objects.all().order_by('-created_at')[:5]
    deals = Deal.objects.all().order_by('-created_at')[:5]
    deal_stages = Deal.objects.values('stage').annotate(count=models.Count('id'))
    
    total_customers = Customer.objects.count()
    total_deals = Deal.objects.count()
    total_value = Deal.objects.aggregate(total=models.Sum('amount'))['total'] or 0
    
    context = {
        'customers': customers,
        'deals': deals,
        'deal_stages': deal_stages,
        'total_customers': total_customers,
        'total_deals': total_deals,
        'total_value': total_value,
    }
    return render(request, 'crm/dashboard.html', context)

@login_required
def customer_list(request):
    customers = Customer.objects.all().order_by('-created_at')
    return render(request, 'crm/customer_list.html', {'customers': customers})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'crm/customer_form.html', {'form': form})

@login_required
def deal_list(request):
    deals = Deal.objects.all().order_by('-created_at')
    return render(request, 'crm/deal_list.html', {'deals': deals})

@login_required
def add_deal(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deal_list')
    else:
        form = DealForm()
    return render(request, 'crm/deal_form.html', {'form': form})
