from django.urls import path
from django.contrib.auth import views as auth_views
from feed import views

urlpatterns = [
    path('', views.feed, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate_account, name='activate'), 
    # path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('feed', views.feed, name='feed'),
    path('search/', views.search, name='search'),
    path('preview/<int:document_id>/', views.preview, name='preview'),
    path('send-email/<int:document_id>/', views.send_email, name='send_email'),

    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
]
