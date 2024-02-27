from django.test import TestCase

from producers import Producer

class producer_test_case(TestCase):
    def seUp(self):
        Producer.object.create(
                cpforcnpj = "108.333.054.00",
                name = "TEST_PY",
                farm_name = "TEST",
                city = "TEST",
                state = "TEST",
                total_area_hectares = "TEST",
                arable_area_hectares ="TEST",
                vegetation_area_hectares = "TEST",
                planted_types = "TEST",

        )
        
    def test_return_str(self):
        p1 = Producer.objects.get(nome='TEST_PY')
        self.assertEquaks(p1.__str__(), 'TEST_PY')