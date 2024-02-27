from urllib import response
from django.test import TestCase
from django.urls import reverse




class pessoa_view_test_case(TestCase):
    
    def test_status_code_200(self):
        response = self.client.get(reverse('ProducersListView'))
        self.assertEquals(response.status_code, 200)
    
    
    def test_template_used(self):
        response = self.client.get(reverse('ProducersListView'))
        self.assertTemplateUsed(response, 'producers.html')
        
    
    def test_status_code_200(self):
        response = self.client.get(reverse('NewProducerCreateView'))
        self.assertEquals(response.status_code, 200)
    
    
    def test_template_used(self):
        response = self.client.get(reverse('NewProducerCreateView'))
        self.assertTemplateUsed(response, 'new_producers.html')
    
    def test_status_code_200(self):
        response = self.client.get(reverse('ProducersListView'))
        self.assertEquals(response.status_code, 200)
    
    
    def test_template_used(self):
        response = self.client.get(reverse('ProducerDetailView'))
        self.assertTemplateUsed(response, 'producer_detail.html')
    
    def test_status_code_200(self):
        response = self.client.get(reverse('ProducerUpdateView'))
        self.assertEquals(response.status_code, 200)
    
    
    def test_template_used(self):
        response = self.client.get(reverse('ProducerUpdateView'))
        self.assertTemplateUsed(response, 'producer_update.html')
    
    
    def test_status_code_200(self):
        response = self.client.get(reverse('ProducerDeleteView'))
        self.assertEquals(response.status_code, 200)
    
    
    def test_template_used(self):
        response = self.client.get(reverse('ProducerDeleteView'))
        self.assertTemplateUsed(response, 'producer_delete.html')
        
    def test_status_code_200(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
    
    
    def test_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')