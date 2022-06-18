from sys import api_version
from django.urls import path
from Api import views as api_views

urlpatterns = [
    path('', api_views.belge_list_create_api_view, name="belge-listesi"),
    path('<int:pk>',api_views.belge_detail_api_view,name='makale-detay')

]