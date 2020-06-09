from django.urls import path
from . import views

# define url addresses to be used in the project
urlpatterns = [
    path("", views.index, name="index"),
    path("<type>/", views.conversion_types, name="conversion_types"),
    path("<type>/accounts/<pk>", views.conversion_types, name="conversion_types_history"),
    path('accounts/signup/', views.signup_view, name="signup_view"),
    path('accounts/login/', views.login_view, name="login_view"),
    path('accounts/logout/', views.log_out_view, name="log_out_view"),
    path('accounts/user_history', views.user_history, name="user_history"),
]
