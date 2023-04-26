from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('phone/<int:id>/', views.index_detail, name='index_detail'),
    path('phone_update/<int:id>/', views.update_detail, name='update_detail'),
    path('phone_delete/<int:id>/', views.delete_detail, name='delete_detail'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('create/', views.create, name='create'),
]
