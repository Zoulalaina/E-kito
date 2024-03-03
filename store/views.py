from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from store.models import Produit, Cart, Order
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def index(request ):
    produits = Produit.objects.all()
    return render(request, 'store/index.html', context={"produits":produits})
def produit_detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    return render(request, 'store/detail.html', context={"produit":produit})

def add_to_cart(request, slug):
    user = request.user
    produit = get_object_or_404(Produit, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    orderr, created = Order.objects.get_or_create(user=user, produit=produit)
    
    if created:
        cart.order.add(orderr)
        cart.save() 
    else:
        orderr.quantity +=1
        orderr.save()

    return redirect(reverse("produit", kwargs={"slug":slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'store/cart.html', context={"orders": cart.order.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.order.all().delete()
        cart.delete()

    return redirect('index')