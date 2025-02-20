from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('blog-details/', views.blog_details_view, name='blog-details'),
    path('shopping-cart/', views.shopping_cart_view, name='shopping-cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('faq/', views.faq_view, name='faq'),
    path('story/', views.story, name='story'),

path('saree/', views.saree, name='saree'),
path('lehenga/', views.lehen, name='lehenga'),
path('western/', views.wesdress, name='western'),
path('customize/', views.customize, name='customize'),
path('casual/', views.casuals, name='casual'),
path('kur/', views.kur, name='kur'),
path('kid/', views.kid, name='kid'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('product/<int:product_id>/', views.purchase_product, name='purchase_product'),
    path('customize/<int:product_id>/', views.customize_product, name='customize'),
path('saree/<int:product_id>/', views.purchased_saree, name='saree'),
path('lehenga/<int:product_id>/', views.purchased_lehenga, name='lehenga'),

path('casuals/<int:product_id>/', views.purchased_casual, name='casuals'),
path('western/<int:product_id>/', views.purchased_western, name='western'),
path('kurtis/<int:product_id>/', views.purchased_kurtis, name='kurtis'),
path('kidd/<int:product_id>/', views.purchased_kidd, name='kidd'),
path('latestt/<int:product_id>/', views.purchase_latest, name='latestt'),
]
