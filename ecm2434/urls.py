from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('articleone/', views.article_one, name='article_one'),
    path('answer/', views.answer, name='answer'),
    path('about/', views.about, name='about'),
    path('priv_pol/', views.priv_pol, name='priv_pol'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('leaderboard/', include('leaderboard.urls')),
    path('scan_qr/', views.scan_qr, name='scan_qr'),
]
