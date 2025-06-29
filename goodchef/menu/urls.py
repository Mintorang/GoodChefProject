from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('items/', views.MenuItemListView.as_view(), name='menu_items'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('checkout/', views.checkout, name='checkout'),
] 