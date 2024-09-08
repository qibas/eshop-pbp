from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = {
        'name': 'nintendo',
        'price': 5000000,
        'description': 'nintendo dengan layar 6 inci',
        'image_url': ''
    }

    context = {
        'products': products,
        'shop_name': 'E-Shop PBP'
    }
    return render(request, "main.html", context)