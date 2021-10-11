from django.urls import path
from clinet import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),

    path('galer_list/', views.galer_list, name="galer_list"),
    path('galer_create/', views.galer_create, name="galer_create"),
    path('<int:pk>galer_edit/', views.galer_edit, name="galer_edit"),
    path('<int:pk>/galer_delete/', views.galer_delete, name="galer_delete"),

    path('product_list/', views.product_list, name="product_list"),
    path('product_create/', views.product_create, name="product_create"),
    path('<int:pk>product_edit/', views.product_edit, name="product_edit"),
    path('<int:pk>/product_delete/', views.product_delete, name="product_delete"),

    path('new_list/', views.new_list, name="new_list"),
    path('new_create/', views.new_create, name="new_create"),
    path('<int:pk>new_edit/', views.new_edit, name="new_edit"),
    path('<int:pk>/new_delete/', views.new_delete, name="new_delete"),

    path('user_list/', views.user_list, name="user_list"),
    path('user_create/', views.user_create, name="user_create"),
    path('<int:pk>user_edit/', views.user_edit, name="user_edit"),
    path('<int:pk>/user_delete/', views.user_delete, name="user_delete"),


]
