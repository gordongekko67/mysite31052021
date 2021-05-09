"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views as views_blog
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from funzioniiot import views as views_app_iot
from myshop import views as views_myshop
from funzioniiot.views import titoloDetailView, TitoloDetailViewCB, home

sitemaps = {
    'posts': PostSitemap,
}



urlpatterns = [
    path('', views_blog.homep),
    path('hellomyshop', views_myshop.myshophello),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('hellocontattaci', views_app_iot.hellocontattaci),
    path('creatitoli', views_app_iot.crea_titoli),
    path('visuatitoli', views_app_iot.visuatitoli),
    path('homeiot', views_app_iot.homeiot),
    path('homeTitoly', views_app_iot.homeTitoly),
    path('modificatitolo', views_app_iot.mod_titoli),
    path('cancellatitolo', views_app_iot.can_titoli),
    path('titoli2/', include('funzioniiot.urls', namespace='titol')),
    path('titoli2/titolosingolo/<int:pk>', titoloDetailView, name ='titolo_detail'),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('account/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)