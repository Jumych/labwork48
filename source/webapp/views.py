from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm


# Create your views here.
def index_view(request):
    eshop = Product.objects.order_by('category')

    context = {
        'eshop': eshop
    }
    return render(request, 'index.html', context)


def eshop_view(request, pk):
    eshop = get_object_or_404(Product, pk=pk)
    return render(request, 'eshop_view.html', {'eshop': eshop})


def add_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form = Product.objects.create(name=form.cleaned_data['name'], price=form.cleaned_data['price'], category=form.cleaned_data['category'])
            return redirect('index')
        else:
            return render(request, 'add_product.html', {'form', form})

def update_product(request, pk):
    eshop = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            'name': eshop.name,
            'description': eshop.description,
            'category': eshop.category,
            'remainder': eshop.remainder,
            'price': eshop.price
        })
        return render(request, "update_product.html", {'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            eshop.name = form.cleaned_data.get('name')
            eshop.description = form.cleaned_data.get('description')
            eshop.category = form.cleaned_data.get('category')
            eshop.remainder = form.cleaned_data.get('remainder')
            eshop.price = form.cleaned_data.get('price')
            eshop.save()
            return redirect('index')
        else:
            return render(request, "update_product.html", {'form': form})

def product_delete(request, pk):
    eshop = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_product.html', context={'eshop': eshop})
    elif request.method == 'POST':
        eshop.delete()
        return redirect('index')







