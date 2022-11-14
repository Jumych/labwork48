from django.shortcuts import render, get_object_or_404
from webapp.models import Product


# Create your views here.
def index_view(request):
    eshop = Product.objects.order_by

    context = {
        'eshop': eshop
    }
    return render(request, 'index.html', context)


def eshop_view(request, pk):
    eshop = get_object_or_404(Product, pk=pk)
    return render(request, 'eshop_view.html', {'eshop': eshop})