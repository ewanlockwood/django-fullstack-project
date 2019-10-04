from django.shortcuts import get_object_or_404
from template_store.models import Template


def cart_contents(request):
    
    cart = request.session.get('get', {})
    
    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_objects_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count }