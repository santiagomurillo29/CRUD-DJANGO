from django.urls import path 
from.import views


urlpatterns = [
    path('select/', views.select),
    path('update/', views.update),
    path('insert/', views.insert),
    path('delete/', views.delete)
      
]
