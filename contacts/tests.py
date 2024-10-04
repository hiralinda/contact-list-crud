from django.test import TestCase
from django.urls import reverse
from .models import Contact

class ContactTests(TestCase):

    def setUp(self):
        Contact.objects.create(name="Joker", email="joker@example.com", phone="123456789")
        Contact.objects.create(name="Harley Quinn", email="harley@example.com", phone="987654321")

    def test_contact_list(self):
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Joker")
        self.assertContains(response, "Harley Quinn")

    def test_create_contact(self):
        response = self.client.post(reverse('contact_create'), {
            'name': 'Batman',
            'email': 'batman@example.com',
            'phone': '555666777'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 3)
        self.assertTrue(Contact.objects.filter(name='Batman').exists())

    def test_update_contact(self):
        contact = Contact.objects.get(name="Joker")
        response = self.client.post(reverse('contact_update', args=[contact.id]), {
            'name': 'Joker Updated',
            'email': 'jokerupdated@example.com',
            'phone': '123456789'
        })
        self.assertEqual(response.status_code, 302)
        contact.refresh_from_db()
        self.assertEqual(contact.name, 'Joker Updated')

    def test_delete_contact(self):
        contact = Contact.objects.get(name="Harley Quinn")
        response = self.client.post(reverse('contact_delete', args=[contact.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 1)

    def test_search_contacts(self):
        response = self.client.get(reverse('contact_list'), {'q': 'joker'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Joker')
        self.assertNotContains(response, 'Harley Quinn')

        response = self.client.get(reverse('contact_list'), {'q': 'harley@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harley Quinn')
        self.assertNotContains(response, 'Joker')
