from django.forms import ModelForm
from .models import Material

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['descricao', 'quantidade' , 'preco']
