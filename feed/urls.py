from django.urls import path
from django.contrib.auth import views as auth_views
from feed import views
from amalitech_file_server.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('', views.feed, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate_account, name='activate'), 
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('feed/', views.feed, name='feed'),
    path('preview/<int:document_id>/', views.preview, name='preview'),
    path('profile/', views.profile, name='profile'),
    path('profile/password_change/', views.change_password, name='password_change'),
    path('documents/downloads/<int:document_id>/', view=views.downloads , name='document_downlaod'),
    path('send-email/<int:document_id>/', views.send_file_email, name='send_email'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
