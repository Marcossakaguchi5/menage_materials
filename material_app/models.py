from django.db import models

class Material(models.Model): 
	descricao = models.CharField(max_length=255,default='')
	quantidade = models.IntegerField(default=0)
	preco = models.FloatField(default=0)  
