from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Item, Client, Order, Message
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
def index_id(request, id):
    return render(request, 'index.html')

'''def home(request):
    if Bag.objects.filter(session=request.session.session_key, validated=False).exists():
        bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
        nb = bag.items.all().count()
    else:
        nb = ''
    return render(request, 'home.html', {'nb': nb})

def products(request):
    products = Product.objects.all()
    if Bag.objects.filter(session=request.session.session_key, validated=False).exists():
        bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
        nb = bag.items.all().count()
    else:
        nb = ''
    return render(request, 'products.html', {'products': products, 'nb': nb})

def product(request, id):
    if Bag.objects.filter(session=request.session.session_key, validated=False).exists():
        bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
        nb = bag.items.all().count()
    else:
        nb = ''
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        size = request.POST['size']
        quantity = request.POST['quantity']
        if size:
            item_total = product.price * int(quantity)
            if Item.objects.filter(size=size, quantity=quantity).exists():
                item = Item.objects.get(size=size, quantity=quantity)
            else:
                item = Item.objects.create(product=product, price=item_total, size=size, quantity=quantity)
                item.save()
            if Bag.objects.filter(session=request.session.session_key, validated=False).exists():
                bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
                if bag.items.filter(size=size).exists():
                    old_item = bag.items.get(size=size)
                    old_item.quantity += int(quantity)
                    old_item.price += item_total
                    bag.total += item_total
                    old_item.save()
                    bag.save()
                    return redirect('/bag')
                else:
                    bag.items.add(item)
                    bag.total += item_total
                    bag.save()
                    return redirect('/bag')
            else:
                if not request.session.session_key:
                    request.session.create()
                bag = Bag.objects.create(session=request.session.session_key, total=item_total)
                bag.items.add(item)
                bag.save()
                return redirect('/bag')
        else:
            messages.info(request, 'You have to select a size!')
            return render(request, 'product.html', {'product': product, 'nb': nb})
    else:
        return render(request, 'product.html', {'product': product, 'nb': nb})

def bag(request):
    bags = Bag.objects.filter(session=request.session.session_key, validated=False)
    if Bag.objects.filter(session=request.session.session_key, validated=False).exists():
        bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
        nb = bag.items.all().count()
    else:
        nb = ''
    return render(request, 'bag.html', {'bag': bags, 'nb': nb})

def remove_item(request, id):
    item = get_object_or_404(Item, id=id)
    bag = get_object_or_404(Bag, session=request.session.session_key ,items=item, validated=False)
    bag.total -= item.price
    if bag.total > 0:
        bag.items.remove(item)
        bag.save()
        return redirect('/bag')
    else:
        bag.delete()
        return redirect('/bag')
    
def order(request):
    bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
    nb = bag.items.all().count()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        bag.validated = True
        bag.save()
        client = Client.objects.create(name=name, email=email, address=address, phone=phone)
        client.save()
        order = Order.objects.create(client=client, bag=bag)
        order.save()
        return redirect('/validated')
    else:
        return render(request, 'order.html', {'bag': bag, 'nb':nb})
    
def validated(request):
    bag = Bag.objects.filter(session=request.session.session_key, validated=True)
    bag = bag.last()
    return render(request, 'validated.html', {'bag': bag})

def contact(request):
    if Bag.objects.filter(session=request.session.session_key, validated=False).exists():
        bag = get_object_or_404(Bag, session=request.session.session_key, validated=False)
        nb = bag.items.all().count()
    else:
        nb = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        client = Client.objects.create(name=name, email=email, phone=phone)
        client.save()
        message = Message.objects.create(client=client, content=message)
        message.save()
        return redirect('/')
    else:
        return render(request, 'contact.html', {'nb': nb})'''
