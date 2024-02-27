from django.test import TestCase
from forms import ProducerModelForm

class producer_form_testcase(TestCase):
    
    def test_producer_form_valid(self):
        form = ProducerModelForm(data={
            'cpforcnpj': "108.333.054.00",
            'name': "TEST_PY",
            'farm_name': "TEST",
            'city': "TEST",
            'state': "TEST",
            'total_area_hectares': 120
            'arable_area_hectares': 80
            'vegetation_area_hectares': 40,
            'planted_types': "TEST",        
        })
        self.assertTrue(form.is_valid())
        
    def test_producer_form_invalid(self):
        form = ProducerModelForm(data={
            self.assertFalse(form.is_valid())
        })