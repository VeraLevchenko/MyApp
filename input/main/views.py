from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Output, Subject
from .form import *


def output_list(request):
	output_list = Output.objects.order_by('-number')
	return render(request, 'main/index.html', {'output_list': output_list})

# *args, **kwargs
def create_output(request, **kwargs):
	error = ''
	if request.method == 'POST':
		form = OutputForm(request.POST)
		if form.is_valid():
			pk = kwargs
			print("!!!!!!!!!!!!!!!", pk)
			# subject_inn = Subject.objects.get(pk=pk)
			form.save()
			return redirect('/')
		else:
			error = 'Форма неверная'
	form = OutputForm()
	data = {
		'form': form,
		'error': error
		# 'subject_inn': subject_inn
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


