import csv

from django.apps import apps
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers import json
from django.db.models.fields import json
from django.http import HttpResponse, response, response
from django.shortcuts import render, redirect
from django.db.models import Q
from django.template import response
from django.template.context_processors import request
from django.views import View

from customer.models import Customer
from customer.forms import CustomerModelForm

# Create your views here.


# def customers(request):
#     search_query = request.GET.get('search', 'Not Found')
#     if search_query:
#         customer_list = Customer.objects.filter(Q(full_name__icontains=search_query) | Q(email__icontains=search_query))
#
#         page = request.GET.get('page', 1)
#         paginator = Paginator(customer_list, 5)
#         try:
#             page_obj = paginator.page(page)
#         except PageNotAnInteger:
#             page_obj = paginator.page(1)
#         except EmptyPage:
#             page_obj = paginator.page(paginator.num_pages)
#         context = {
#             'page_obj': page_obj,
#         }
#         return render(request, 'customer/customer_list.html', context)


class CustomersView(View):
    def get(self, request):
        search_query = request.GET.get('search', 'Not Found')
        if search_query:
            customer_list = Customer.objects.filter(Q(full_name__icontains=search_query) | Q(email__icontains=search_query))

            page = request.GET.get('page', 1)
            paginator = Paginator(customer_list, 5)
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            context = {
                 'page_obj': page_obj,
                }
            return render(request, 'customer/customer_list.html', context)


# def add_customer(request):
#     form = CustomerModelForm()
#     if request.method == 'POST':
#         form = CustomerModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('customers')
#     context = {
#         'form': form,
#     }
#     return render(request, 'customer/add_customer.html', context)

class AddCustomerView(View):
    def get(self, request):
        form = CustomerModelForm()
        if request.method == 'POST':
            form = CustomerModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('customers')
        context = {
            'form': form
        }
        return render(request, 'customer/add_customer.html', context)


# def delete_customer(request, pk):
#     customer = Customer.objects.get(id=pk)
#     if customer:
#         customer.delete()
#         messages.add_message(
#             request,
#             messages.SUCCESS,
#             'Customer successfully deleted'
#         )
#         return redirect('customers')

class DeleteCustomerView(View):
    def get(self, request):
        customer = Customer.objects.get(id=pk)
        if customer:
            customer.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Customer successfully deleted'
            )
            return redirect('customers')

# def edit_customer(request, pk):
#     customer = Customer.objects.get(id=pk)
#     form = CustomerModelForm()
#     if request.method == 'POST':
#         form = CustomerModelForm(data=request.POST, files=request.FILES, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('customers')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'customer/update_customer.html', context)

class EditcustomerView(View):
    def get(self, request, pk):
        customer = Customer.objects.get(id=pk)
        form = CustomerModelForm()
        if request.method == 'POST':
            form = CustomerModelForm(data=request.POST, files=request.FILES, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('customers')

        context = {
            'form':form
        }
        return render(request,'customer/update_customer.html', context)


def export_data(request):
    format = request.GET.get('format', 'csv')
    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=customers.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'Full Name', 'Email', 'Phone Number', 'Address'])
        for customer in Customer.objects.all():
            writer.writerow([customer.id, customer.full_name, customer.email, customer.phone_number, customer.address])


    elif format == 'json':
        response = HttpResponse(content_type='application/json')
        data = list(Customer.objects.all().values('full_name', 'email', 'phone_number', 'address'))
        response.write(json.dumps(data, indent=4))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
    elif format == 'xlsx':
        pass

    else:
        response = HttpResponse(status=404)
        response.content = 'Bad request'

    return response

