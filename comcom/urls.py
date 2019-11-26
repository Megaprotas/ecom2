from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from core import views as core_views
from cart import views as cart_views
from checkout import views as checkout_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('cart/', cart_views.cart, name='cart'),
    path('checkout/', checkout_views.checkout, name='checkout'),
    path('cart/<id>/', cart_views.edit_cart, name='edit_cart'),
    path('profile/', accounts_views.profile, name='profile'),
    path('aboutus/', accounts_views.aboutus, name='aboutus'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('register/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
