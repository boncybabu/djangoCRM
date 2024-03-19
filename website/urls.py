from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('records/<int:pk>',views.customer_records,name='records'),
    path('delete_records/<int:pk>',views.delete_records,name='delete_records'),
    path('add_records/',views.add_records,name='add_records'),
    path('update_records/<int:pk>',views.update_records,name='update_records'),
  
]
