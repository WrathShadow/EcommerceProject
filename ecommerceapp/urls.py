from django.urls import path, include
from . import views
app_name='ecommerceapp'
urlpatterns=[
    path('cart/',include("cart.urls")),
    path('',views.allProdCat,name='allProdCat'),
    path('login',views.login,name='login'),
    path('search/',include('search_app.urls')),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name='ProdCatDetail'),
]