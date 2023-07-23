from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Output, Subject
from .form import *


def output_list(request):
	output_list = Output.objects.order_by('-time_create')
	return render(request, 'main/index.html', {'output_list': output_list})

# *args, **kwargs
def create_output(request):
	error = ''
	if request.method == 'POST':
		form = OutputForm(request.POST, request.FILES)
		img_obj = form.instance
		print("form.instance", img_obj)
		if form.is_valid():
			print("11111111111111111111111")
			form.save()
			return redirect('/')
		else:
			print("22222222222222222222")
			error = 'Форма неверная'
	form = OutputForm()
	data = {
		'form': form,
		'error': error
	}
	return render(request, 'main/create_output.html', data)


def output_details(request, pk):
	output_details = Output.objects.get(pk=pk)
	return render(request, 'main/output_details.html', {'output_details': output_details})



# импорт модели Artists

# class OutputView(generic.ListView):
# 	model = Output
# 	template_name = 'main/base.html'
# 	context_object_name = 'output_list'
# 	print("dfgadgfadfg", context_object_name[1])


