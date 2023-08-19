from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
	path('search/', SearchResultsView.as_view(), name='search_results'),
	path('', OutputList.as_view(), name='output_list'),
	re_path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
	path('create_output', views.create_output, name='create_output'),
	path('<int:pk>', views.output_details, name='output_details'),
    ]

