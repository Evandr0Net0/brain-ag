from django import forms
from . import models


class ProducerModelForm(forms.ModelForm):

    class Meta:
        model = models.Producer
        fields = ['cpforcnpj', 'name', 'farm_name',
                  'city', 'state', 'total_area_hectares', 'arable_area_hectares',
                  'vegetation_area_hectares', 'planted_types']
        widgets = {
            'cpforcnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'total_area_hectares': forms.NumberInput(attrs={'class': 'form-control'}),
            'arable_area_hectares': forms.NumberInput(attrs={'class': 'form-control'}),
            'vegetation_area_hectares': forms.NumberInput(attrs={'class': 'form-control'}),
            'planted_types': forms.TextInput(attrs={'class': 'form-control'}),


        }

        labels = {
            'cpforcnpj': 'CPF/CNPJ',
            'name': 'Nome',
            'farm_name': 'Nome da Fazenda',
            'city': 'Cidade',
            'state': 'Estado',
            'total_area_hectares': 'Área Total (HECTARES)',
            'arable_area_hectares': 'Área Agricultável (HECTARES)',
            'vegetation_area_hectares': 'Área de Vegetação (HECTARES)',
            'planted_types': 'Culturas Plantadas',

        }


class CreatedProducerModelForm(forms.ModelForm):

    class Meta:
        model = models.Producer
        fields = ['cpforcnpj', 'name', 'farm_name',
                  'city', 'state', 'total_area_hectares', 'arable_area_hectares',
                  'vegetation_area_hectares', 'planted_types']
        widgets = {
            'cpf_cnpj': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'total_area_hectares': forms.NumberInput(attrs={'class': 'form-control'}),
            'arable_area_hectares': forms.NumberInput(attrs={'class': 'form-control'}),
            'vegetation_area_hectares': forms.NumberInput(attrs={'class': 'form-control'}),
            'planted_types': forms.TextInput(attrs={'class': 'form-control'}),



        }
        labels = {
            'cpf_cnpj': 'CPF/CNPJ',
            'name': 'Nome',
            'farm_name': 'Nome da Fazenda',
            'city': 'Cidade',
            'state': 'Estado',
            'total_area_hectares': 'Área Total (HECTARES)',
            'arable_area_hectares': 'Área Agricultável (HECTARES)',
            'vegetation_area_hectares': 'Área de Vegetação (HECTARES)',
            'planted_types': 'Culturas Plantadas',

        }
