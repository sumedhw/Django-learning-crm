from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage , name="register"),
    path('login/', views.loginPage , name='login'),
    path('logout/', views.logoutUser , name='logout'),

    path('' , views.home , name='home') ,
    path('user/', views.userPage, name="user-page"),

    path('account/', views.accountSettings, name="account"),

    path('products' , views.products , name='products') ,
    path('customer/<str:pk_test>/' , views.customer , name='customer') ,

    path('createOrder/<str:pk>' ,  views.createOrder , name='create_order'),
    path('updateOrder/<str:pk>' ,  views.updateOrder , name='update_order'),
    path('deleteOrder/<str:pk>' ,  views.deleteOrder , name='delete_order')
]