from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.get_queryset, name='index.html'),
	path('result/', views.result),
    path('result', views.result, name='result'),
	re_path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
	path('create_output', views.create_output, name='create_output'),
	path('<int:pk>', views.output_details, name='output_details'),
    ]

