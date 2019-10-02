from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:agency_id>/',views.agency_detail, name = 'agency_detail' ),
]