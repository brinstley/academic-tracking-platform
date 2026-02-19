from django.urls import path

from accounts import views

urlpatterns = [
    path('create/', views.createAccount.as_view(), name='account-create'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('password-reset/', views.passwordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/', views.passwordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-change/', views.passwordChangeView.as_view(), name='password-change'),
    path('password-change-confirm/', views.passwordChangeConfirmView.as_view(), name='password-change-confirm'),
]
