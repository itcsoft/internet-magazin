from django.urls import path
from .views.homepage import homepage
from .views.detail import detail
from .views.cart import cart, addToCard, remove_from_cart
from .views.register import register
from .views.signin import signin
from .views.signout import signout
# from .views.cartAdd import cartAdd
from .views.category import pr_by_category


urlpatterns = [
  path('', homepage, name='homepage'),
  path('detail/<int:pk>', detail, name='detail'),
  path('cart/', cart, name='cart'),            
  path('register', register, name='register'),   #регистрация
  path('signin', signin, name='signin'),         #авторизация, (войти)
  path('signout', signout, name='signout'),       #выход
  path('addToCard/<int:pk>', addToCard, name='addToCard'),
  path('remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
  path('category/<int:pk>', pr_by_category, name='pr_by_category')
] 