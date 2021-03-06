from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
	path('',HomeView.as_view(),name='home'), # since we are using class based views
	path('subcategory/<slug>',SubCategoryView.as_view(),name='subcategory'),
	path('brand/<slug>',BrandView.as_view(),name='brand'),
	path('detail/<slug>',DetailView.as_view(),name='detail'),
	path('review',review,name='review'),
	path('signup',signup,name='signup'),
	path('add-to-cart',add_to_cart,name='add-to-cart'),
	path('cart',CartView.as_view(),name='cart'),

]