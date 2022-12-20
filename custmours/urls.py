from django.urls import path
from . import views
urlpatterns = [
      path('reg/',views.register, name = 'reg'),
      path('login/',views.auth_login, name = 'login'),
      path('logout/', views.logoutpage, name = 'logout'),
      path('account/',views.account,name = 'account'),
      path('address/',views.address, name = "address")
      # path('orders/', views.orders, name= 'orders')
]