from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person

class PersonAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {'name': 'John Doe', 'age': 30}
        self.url = reverse('person-list-create')

    def test_create_person(self):
        response = self.client.post(self.url, self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)

    def test_get_person(self):
        person = Person.objects.create(name='Jane Smith', age=25)
        url = reverse('person-detail', args=[person.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Smith')

    def test_update_person(self):
        person = Person.objects.create(name='Tom', age=40)
        url = reverse('person-detail', args=[person.id])
        updated_data = {'name': 'Tom Smith', 'age': 42}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tom Smith')

    def test_delete_person(self):
        person = Person.objects.create(name='Delete Me', age=30)
        url = reverse('person-detail', args=[person.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
