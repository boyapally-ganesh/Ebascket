from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Category, product,cart, wishlist, order, orderitem
from django.contrib import messages
from custmours.models import profile
# from .forms import customuserform
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib.auth.models import User
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def navbar(request):
    # mobileitem = product.objects.filter(category="Mobiles", status=0)
    cateitems = Category.objects.filter(status=0)
    context = {'mobile':cateitems}
    return render(request, 'products/navbar2.html',context)

def home(request):
    # if(Category.objects.filter(slug="mobiles", status=0)):
    products = product.objects.filter(category__slug="mobiles")
    productsclothes = product.objects.filter(category__slug="clothes")
    productsgadgets = product.objects.filter(category__slug="gadgets")
    productsshoes = product.objects.filter(category__slug="shoes")
    category_name = Category.objects.filter(slug="mobiles").first()
        # context = {'products':products, 'category_name':category_name}
        # return render(request, 'products/collectionview.html', context)
    # else:
    #     messages.warning(request, 'no such category found')
    #     return redirect('collections')
    # one comment
    cotegory = Category.objects.filter(status=0)
    trandingproducts = product.objects.filter(tranding=1)
    context = {'tranding':trandingproducts,'category':cotegory, 'productname':products,'productgadgets':productsgadgets,'productclothes':productsclothes,'productshoes':productsshoes}
    return render(request, 'products/main.html', context)
# def category(request):
#     return render(request, 'products\category.html')
# def checkout(request):
    # return render(request, 'products/checkout.html')
def colllections(request):
    cotegory = Category.objects.filter(status=0)
    context = {'category':cotegory}
    return render(request, 'products/collections.html', context)
# def collectionview(request):
#     return render(request, 'products/collectionview.html')
def collentionview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category_name':category_name}
        return render(request, 'products/collectionview.html', context)
    else:
        messages.warning(request, 'no such category found')
        return redirect('collections')
#productview
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status =0)):
         if(product.objects.filter(slug=prod_slug, status =0)):
             products = product.objects.filter(slug=prod_slug, status =0).first()
             context = {'products':products}

         else:
           messages.error(request, 'no such category found')
           return redirect("collentions")
    else:
        messages.error(request, 'no such category found')
        
        return redirect("collentions")
    return render(request, 'products/productview.html', context)
#add to cart
@csrf_exempt
def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = product.objects.get(id=prod_id)
            if(product_check):
                if(cart.objects.filter(user=request.user.id, product_id=prod_id)):
                     return JsonResponse({"status":'product all ready in cart'})
                     messsage.error(request, 'prodcut all ready in cart')
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty :
                        cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({"status":'product add sucessfully'})
                    else:
                         return JsonResponse({"status":'only '+ str(product_check.quantity) + "quenity available"})
            else:
                return JsonResponse({"status":'no such product found'})
        else:
            return JsonResponse({'status': 'login to continue'})
    return redirect('/')
@login_required(login_url='login')
def viewcart(request):
    carts = cart.objects.filter(user=request.user)
    context = {'carts':carts}
    return render(request, "products/viewcart.html",context)
#update cart
def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            Cart = cart.objects.get(product_id=prod_id, user=request.user)
            Cart.product_qty = prod_qty
            Cart.save()
            return JsonResponse({'status':'product updated successfully'})
    return redirect('/')
# delete cart item
def removecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_ids'))
        if(cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status':'deleted succesfully'})
    return redirect('/')
#wishlist view
@login_required(login_url='login')
def likedproducts(request):
    wishlists = wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlists}
    return render(request, 'custmour/wishlist.html', context)
# add to wishlist
@login_required(login_url='login')
def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = product.objects.get(id=prod_id)
            if(product_check):
                if(wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':'product already in wishlist'})
                else:
                    wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':'product added to wishlist'})
            else:
                return JsonResponse({'status':'no such product found'})  
        else:
            return JsonResponse({'status':'login to continue'}) 
    return redirect('/') 
# delte wishlist item 
@login_required(login_url='login')
def deletewishitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('products_ids')) 
            if(wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':'product removed form wishlist'}) 
            else:
                return JsonResponse({'status':'product not found in wishlist'})
        return JsonResponse({'status':'login to continue'})
    return redirect('/')
# def wishlist(request):
#     return render(request, 'custmour/account.html')
# def dcart(request):
#     return render(request, 'products/cards.html')
#check out
@login_required(login_url='login')
def checkout(request):
    rawcart = cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            cart.objects.delete(id=item.id)
    cartitems = cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    userprofile = profile.objects.filter(user=request.user).first()
    context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile': userprofile}
    return render(request, 'products/checkout.html', context)
#chechout complete
@login_required(login_url='login')
def placeorder(request):
    if request.method == "POST":
        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name :
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not profile.objects.filter(user=request.user):
            userprofile = profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()
        neworder = order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')
        neworder.payment_mode = request.POST.get('payment_mode')
        
        Cart = cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in Cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = 'sharma'+str(random.randint(1111111, 9999999))
        while order.objects.filter(tracking_no=trackno) is None:
            trackno = 'sharma'+str(random.randint(1111111, 9999999))
        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = cart.objects.filter(user=request.user)
        for item in neworderitems:
            orderitem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )

            # to decrease the product quantity from available stock
            orderproduct = product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()
        # to clear user's cart
        cart.objects.filter(user=request.user).delete()

        paymod = request.POST.get('payment_mode')
        if (paymod == "paid by paypal"):
             return JsonResponse({"status":'your order placed succesfully'})
        else:
          messages.success(request, 'your order has been placed successfully')

    return redirect('/')  
def ordercomplete(request):
    # odercm = order.objects.filter(user=request.user)
    # context = {'ordercomplete':odercm}
    return render(request, 'products/sli.html')
#orders history
def myorder(request):
    orders = order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, 'custmour/orderhistory.html', context)
#total orderscompltet

#product search
def productsearch(request):
    products = product.objects.filter(status=0).values_list('name', flat=True)
   
    productlist = list(products)

    return JsonResponse(productlist, safe=False)
#search product ietm using form
def searchproductsitem(request):
    if request.method == "POST":
         searcheditem = request.POST.get('searchitem')
         if searcheditem == "":
            return redirect(request, META.get('HTTP_REFERER'))
         else:
            products = product.objects.filter(name__contains=searcheditem).first()

            if products:
                return redirect('collections/'+products.category.slug+'/'+products.slug)
            else:
                  messages.info(request, "no product match your search")
                  return redirect(request.META.get('HTTP_REFERER'))
                
    return redirect(request.META.get('HTTP_REFERER'))
def error_404_view(request, exception):
       
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'products\errorpage.html')
 