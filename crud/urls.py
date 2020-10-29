from django.urls import path
from crud import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [  
    path('', views.Test.first_page, name='Home Page'),   
    path('save_model', views.Test.save_my_model, name='Save Model'),
    path('delete_model', views.Test.delete_model, name='Delete Model'),
    path('edit_model', views.Test.edit_model, name='Edit Model'),
    path('update_model', views.Test.update_model, name='Update Model'),
    path('books', views.Test.getBooks, name='Books Page'),

]