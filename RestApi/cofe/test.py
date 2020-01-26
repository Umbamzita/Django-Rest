from rest_framework.test import APITestCase
from .models import *
from .views import *
from .serializers import *
from django.contrib.auth.models import User



class ReadTest(APITestCase):
  
    def test_view_drinks(self): 
        resp = self.client.get('/api/v1/cofe/drinks/') 
        serializer = DrinkDetailSerializers
        self.assertEqual(resp.status_code, 200) 
        self.assertTrue(resp.json, serializer.data)
        
   
    def test_view_sales(self): 
        resp = self.client.get('/api/v1/cofe/sales/') 
        self.assertEqual(resp.status_code, 403) 


    def test_view_workers(self):
        resp = self.client.get('/api/v1/cofe/workers/')
        serializer = WorkerDetailSerializers
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json, serializer.data)


class ReadSalesTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@mail.ru', 'john')
        self.client.login(username='john', password='john')
        self.user = User.objects.create(username="Ola")
        

    def test_can_read_sales_list(self):
        resp = self.client.get('/api/v1/cofe/sales/')
        self.assertEqual(resp.status_code, 200)


    def test_can_read_sales_detail(self):
        resp = self.client.get('/api/v1/cofe/sales/', args=[self.user.id])
        serializer = SaleSerializers
        self.assertTrue(resp.json, serializer.data)
        self.assertEqual(resp.status_code, 200)


class UpdateDrinksTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'john')
        self.client.login(username='john', password='john')
        self.drink = Drink.objects.create(title='Margarita', price =2)
        self.data = DrinkDetailSerializers(self.drink).data
        self.data.update({'price': 22})
        self.new_drink = {'title' : 'Vodka', 'price' : '10'}


    def test_can_update_drinks(self):
        response = self.client.put(
            '/api/v1/cofe/drinks/'+str(self.drink.id),
            data=self.data,
            follow = True
        )
        self.assertEqual(response.status_code, 200)


    def test_view_drinks_detail(self): 
        resp = self.client.get('/api/v1/cofe/drinks/', args=[self.drink.id]) 
        self.assertEqual(resp.status_code, 200) 


    def test_can_create_drinks(self):
        response = self.client.post('/api/v1/cofe/drinks/', data = {'title' : 'Vodka', 'price' : 1.99}, format='json')
        self.assertEqual(response.status_code, 201)

