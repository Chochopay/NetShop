from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from catalog.models import Category


def home(request):
    products = Product.objects.all()

    return render(
        request,
        'catalog/home.html',
        {'products': products}
    )

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("/")

    return render(request, "catalog/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("/")

        return render(
            request,
            "catalog/login.html",
            {"error": "Неверный логин или пароль"},
        )

    return render(request, "catalog/login.html")


@login_required
def create_product(request):
    if request.method == "POST":
        Product.objects.create(
            author=request.user,
            category_id=request.POST["category"],
            name=request.POST["name"],
            description=request.POST["description"],
            price=request.POST["price"],
            image=request.FILES.get("image"),
        )

        return redirect("/")

    categories = Category.objects.all()

    return render(
        request,
        "catalog/create_product.html",
        {"categories": categories},
    )