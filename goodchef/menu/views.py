from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, MenuItem

def menu_list(request):
    """Display all menu categories with their items."""
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu/menu_list.html', {
        'categories': categories
    })

def category_detail(request, category_id):
    """Display items in a specific category."""
    try:
        category = Category.objects.get(id=category_id)
        items = category.items.all()
        return render(request, 'menu/category_detail.html', {
            'category': category,
            'items': items
        })
    except Category.DoesNotExist:
        return render(request, 'menu/404.html', status=404)

def about_us(request):
    """About Us page."""
    return render(request, 'menu/about.html')

def contact(request):
    """Contact page."""
    return render(request, 'menu/contact.html')

def delivery(request):
    """Delivery information page."""
    return render(request, 'menu/delivery.html')

def checkout(request):
    """Checkout page."""
    return render(request, 'menu/checkout.html')

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/menu_items.html'
    context_object_name = 'menu_items'
    paginate_by = 20

    def get_queryset(self):
        return MenuItem.objects.select_related('category').all()

class CategoryListView(ListView):
    model = Category
    template_name = 'menu/categories.html'
    context_object_name = 'categories' 