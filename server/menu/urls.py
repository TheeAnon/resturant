from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.menu_items, name='menu_items'),
    path('item/<int:id>/', views.menu_item, name='menu_item'),
    path('categories/', views.categories, name='categories'),
    path('categorized/', views.categorized_menu_items, name='categorized_items'),
    path('create/item/', views.create_menu_item, name='create menu item'),
    path('create/category/', views.create_category, name='create category'),
]