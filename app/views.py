from app.forms import ProductForm
from app.models import Product
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Customer
from app.forms import CustomerForm

# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
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


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'app/add_customer.html', {'form': form})


