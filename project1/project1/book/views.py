from django.shortcuts import render
from .models import books
from django.template.loader import render_to_string
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
def list(request):
    Data = {'allBooks': books.objects.all().order_by("id")}
    return render(request, 'book/sachBanChay.html', Data)

def eachItem(request, id):
    eachItem = books.objects.get(id=id)
    return render(request, 'book/eachItem.html', {'eachItem': eachItem})

def list2(request):
    Data = books.objects.filter(type="STH")
    return render(request, 'book/sachTinHoc.html', {'Data': Data})

def list3(request):
    Data = books.objects.filter(type="SNV")
    return render(request, 'book/sachNhanVan.html', {'Data': Data})

def list4(request):
    Data = books.objects.filter(discount="True")
    return render(request, 'book/sachGiamGia.html', {'Data': Data})

html = render_to_string('book/addcart.html')
cart = {}
itemCart = {}
def addcart(request, id):    
    if request.is_ajax():
        global html
        global itemCart
        id = request.POST.get('id')
        num = request.POST.get('num')
        eachItem = books.objects.get(id=id)
        price = books.objects.get(price=eachItem.price)
        total = books.objects.get(price=eachItem.price)
        if id in cart.keys():
            itemCart = {
                'title': eachItem.title,
                'price': eachItem.price,
                'num': int(cart[id]['num']) + int(num),               
            }
        else:
            itemCart = {
                'title': eachItem.title,
                'price': eachItem.price,
                'num': int(num),                            
            }
        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']
        html = render_to_string('book/addcart.html', {'cart': cartInfo})

    return HttpResponse(html)

def shoppingCart(request):
    total = 0;   
    for key, value in cart.items():
        total += float(value['price']) * int(value['num'])
    return render(request, 'book/shoppingCart.html', {'total': total})

def deleteItem(request, id):
    id = request.POST.get('key')
    cart = request.session['cart']
    global html
    if request.is_ajax():
        del cart[id]
        request.session['cart'] = cart
        cart = request.session['cart']
        html = render_to_string('book/itemDelete.html', cart)

    return HttpResponse(html)