from django.urls import path
from .import views
from .views import ChartData

urlpatterns = [
    path('index/', views.home, name='home'),
    path('', views.index, name='index'),
    path('api/chat/data/', ChartData.as_view()),
    path('post-entry/', views.post_entry, name='post-entry'),
]