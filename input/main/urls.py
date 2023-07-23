from django.urls import path
from . import views

urlpatterns = [
	path('', views.output_list, name='output_list'),
	path('create_output', views.create_output, name='create_output'),
	path('<int:pk>', views.output_details, name='output_details'),
    ]

