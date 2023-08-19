from datetime import datetime
from itertools import chain

import xlwt
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Output, Subject
from .form import *
from django.utils import timezone
from django.views.generic import ListView
# from haystack.query import SearchQuerySet

class OutputList(ListView):
	model = Output
	template_name = 'main/index.html'  # по умолчанию object_list.html
	context_object_name = 'output_list' # по умолчанию object_list
	queryset = Output.objects.order_by('-time_create')



# *args, **kwargs
def create_output(request):
	error = '!!!!!!!!!!!!!!!!!!'
	if request.method == 'POST':
		print(request.POST)
		form = OutputForm(request.POST, request.FILES)
		if form.is_valid():
			print("11111111111111111111111")
			form.save()
			return redirect('/')
		else:
			print("22222222222222222222")
			error = 'Форма неверная'
	form = OutputForm()
	ctx = {
		'form': form,
		'error': error
	}
	return render(request, 'main/create_output.html', ctx)

def export_users_xls(request):
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="Output.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Output')

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['Исходящий номер', 'Исходящая дата', 'Входящий номер', 'Получатель', 'Краткое содержание', 'Вложение', 'Исполнитель']

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	rows = Output.objects.all()
	datas = []
	for row in rows:
		datas.append([i for i in [row.number,
								 row.data,
								 row.input,
								 row.subject.name,
								 row.info,
								 str(row.doc),
								 row.author
								 # str(row.time_create)
								 ]])

	for data in datas:
		row_num += 1
		for col_num in range(len(data)):
			ws.write(row_num, col_num, data[col_num], font_style)

	wb.save(response)
	return response

def output_details(request, pk):
	output_details = Output.objects.get(pk=pk)
	return render(request, 'main/output_details.html', {'output_details': output_details})


class SearchResultsView(ListView):
	model = Output
	template_name = 'main/search_results.html'

	def get_queryset(self):  # новый
		query = self.request.GET.get("q")
		output_list = Output.objects.filter(
			Q(number__icontains=query) | Q(data__icontains=query) |
			Q(input__icontains=query) | Q(info__icontains=query) |
			Q(subject__name__icontains=query) | Q(author__icontains=query)
		)
		object_list = output_list.order_by('-time_create')
		return object_list


