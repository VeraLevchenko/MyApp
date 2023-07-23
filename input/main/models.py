from django.db import models
from datetime import date


class Subject(models.Model):
	TYPE = [
		(0, "физлицо"),
		(1, "юрлицо")
	]

	name = models.CharField(max_length=254)
	inn = models.IntegerField()
	type_subject = models.CharField(max_length=254, choices=TYPE)

	def __str__(self):
		return f'{self.name}'


class Output(models.Model):
	number = models.IntegerField(editable=True)
	data = models.DateField(editable=True, default=date.today())
	input = models.CharField(max_length=50, default='отсутствует')
	subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
	info = models.CharField(max_length=254)
	doc = models.FileField(blank=False)
	author = models.CharField(max_length=50)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.number} от {self.data}'

# from main.models import Output

# a = Output(number=6, data= datetime.date(2023, 12, 4), subject=Subject.objects.all()[0], info='Краткое содержание', doc="Непонятно", author = 'Жаворонкова')