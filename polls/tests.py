from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class testQuestions(TestCase):

    def test_index_load(self):
        """
        Check that the status_code response from the index page is equal to 200.
        """
        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertTrue(response.status_code == 200)

    def test_invalid_page(self):
        """
        Check that the status_code response from a non-existant question number is a 404
        """
        url = reverse('polls:results', args=('3'))
        response = self.client.get(url)
        self.assertTrue(response.status_code == 404)