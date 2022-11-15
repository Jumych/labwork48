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
