from django.contrib import messages
from django.shortcuts import render, redirect

from customer.models import Customer
from customer.forms import CustomerModelForm

# Create your views here.


def customers(request):
    customer_list = Customer.objects.all()
    context = {
        'customer_list': customer_list,
    }
    return render(request, 'customer/customer_list.html', context)


def add_customer(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    context = {
        'form': form,
    }
    return render(request, 'customer/add_customer.html', context)


def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if customer:
        customer.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Customer successfully deleted'
        )
        return redirect('customers')


def edit_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(data=request.POST, files=request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {
        'form': form
    }
    return render(request, 'customer/update_customer.html', context)