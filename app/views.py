from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from app.forms import ProductForm
from app.models import Product
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from customer.forms import CustomerModelForm
from customer.models import Customer


# Create your views here.


def index(request):
    page = request.GET.get('page', '')
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 2)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes =product.get_attributes()
    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product_detail.html', context)


def add_product(request):
    # form = ProductForm()
    # form = None
    if request.method == 'POST':
        form = ProductForm(request.POST)
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        rating = request.POST['rating']
        discount = request.POST['discount']
        quantity = request.POST['quantity']
        product = Product(name=name, description=description, price=price, discount=discount, quantity=quantity, rating=rating)

        if form.is_valid():
            product.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'app/add_product.html', context)


def customer_list(request):
    users = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'users': users})


def customer_detail(request, customer_id):
    users = Product.objects.get(id=customer_id)
    attributes =users.get_attributes()
    context = {
        'users': users,
        'attributes': attributes
    }
    return render(request, 'customer/customer_detail.html', context)


def add_customer(request):
    if request.method == 'POST':
        form = CustomerModelForm()
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        joined = request.POST['joined']
        users = Customer(full_name=full_name, phone=phone, email=email, address=address, joined=joined)

        if form.is_valid():
            users.save()
            return redirect('customer_list')
        else:
            print(form.errors)
    else:
        form = CustomerModelForm()
    return render(request, 'customer/add_customer.html', {'form': form})




