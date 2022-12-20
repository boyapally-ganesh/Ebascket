from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('navbar2',views.navbar),
    
    path('checkout',views.checkout),
    # path('collectionview', views.collectionview),
    path('collections/',views.colllections, name='collections'),
    path('collections/<str:slug>/',views.collentionview, name = 'collectionview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name = 'productview'),
    #add to cart
    path("add-to-cart",views.addtocart, name = 'addtocard'),
    path('cart', views.viewcart, name = 'cart'),
    path('update-cart',views.updatecart, name = 'updatecart'),
    path('deletecartitem',views.removecart, name = 'delete_cart'),
    path('wishlist',views.likedproducts, name = 'wishlist'),
    path('add-to-wishlist',views.addtowishlist, name = 'addtowishlist'),
    path('deletewishlistitem',views.deletewishitem, name = 'deletewishlistitem'),
    path('checkout',views.checkout, name = 'checkout'),
    # path('wishlist', views.wishlist),
    # path('cards/', views.dcart, name = 'card'),
    path('place-order',views.placeorder, name='placeorder'),
    path('my-orders',views.myorder, name='orders'),
    path('product-list',views.productsearch, name = 'productsearch'),
     #search productitem using form
    path('searchproductsitem', views.searchproductsitem, name = 'searchproductsitem'),
    path('ordercomplate/',views.ordercomplete , name = 'ordercomplate'),
    #  path('view-order/', views.vieworder, name='vieworder'),
]