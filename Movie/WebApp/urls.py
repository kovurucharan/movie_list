from django.urls import path,include
from  WebApp.views import Movie_listAV,Movie_detailsAV
urlpatterns = [
    path('list/',Movie_listAV.as_view()),
    path('<int:pk>',Movie_detailsAV.as_view()),
    
]