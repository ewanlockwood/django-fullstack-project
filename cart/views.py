from django.shortcuts import render

# Create your views here.
def view_cart(request):
    ''' A view that renders all contents of the cart '''
    
    return render(request, 'cart.html')
    
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))