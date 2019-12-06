from django.test import TestCase
import unittest
from core.models import Client

class ClientTest(unittest.TestCase):
    def setUp(self):
        self.jorge = Client.objects.create(first_name="Jorge", last_name="Silva", cpf="333.333.333-34", birth="1999-05-20", address="dajsgafbkvfd")

    def testGetFullNAme(self):
        self.assertEquals(self.jorge.get_full_name(), 'Jorge Silva')
        self.assertEquals(self.jorge.get_full_name(), 'Jorge Carvalho')


        

