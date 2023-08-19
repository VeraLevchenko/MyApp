from django.db import models
from django.utils import timezone


class Subject(models.Model):
	TYPE = [
		("физлицо", "физлицо"),
		("юрлицо", "юрлицо")
	]

	name = models.CharField(max_length=254)
	adress = models.CharField(max_length=254)
	tel = models.SlugField(max_length=50, default='8(111)1111111')
	snils = models.SlugField(max_length=50, blank=False)
	inn = models.IntegerField()
	type_subject = models.CharField(max_length=10, choices=TYPE)

	def __str__(self):
		return f'{self.name}'


class Output(models.Model):
	number = models.IntegerField(editable=True)
	data = models.DateField(editable=True, default=timezone.now)
	input = models.CharField(max_length=50, default='отсутствует')
	subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
	info = models.CharField(max_length=254)
	doc = models.FileField(upload_to="doc/%Y/%m/%d")
	author = models.CharField(max_length=50, editable=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.number} от {self.data}'

# from main.models import Output

# a = Output(number=6, data= datetime.date(2023, 12, 4), subject=Subject.objects.all()[0], info='Краткое содержание', doc="Непонятно", author = 'Жаворонкова')