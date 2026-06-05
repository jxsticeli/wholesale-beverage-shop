from .models import Order
from django.db.models import Sum
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.shortcuts import redirect

from django.shortcuts import render
from .models import Product, Category

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def products(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category__id=category)

    return render(
        request,
        'products.html',
        {
            'products': products,
            'categories': categories
        }
    )
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

def sales_report(request):

    total_orders = Order.objects.count()

    total_revenue = (
        Order.objects.aggregate(
            Sum('total_amount')
        )['total_amount__sum']
        or 0
    )

    return render(
        request,
        'sales_report.html',
        {
            'total_orders': total_orders,
            'total_revenue': total_revenue
        }
    )