from datetime import datetime

from django.test import TestCase

# Create your tests here.
from inv.models import Item, Brand



class ItemTestCase(TestCase):

    def setUp(self):

        self.testElem = Item()
        self.testElem.reference = 45458069
        self.testElem.date_exp = datetime(2022, 8, 25)
        self.testElem.brand = "Test"
        self.testElem.save()


    def test_create_item(self):
        nb_items_before_add = Item.objects.count()
        new_item = Item()
        new_item.reference = 88880000
        new_item.date_exp = datetime.today()
        new_item.brand = "Test"
        new_item.save()

        nb_items_after_add = Item.objects.count()
        self.assertTrue(nb_items_after_add == nb_items_before_add + 1)

        #ajouter un objet dans notre db
        #valider que le nombre d'objets dasn notre db a été incrémenté de 1

        # probeleme d'asert a cause du format de la date

    def test_update_date_exp_item(self):
        self.assertEqual(self.testElem.reference, 45458069)
        self.testElem.date_exp = datetime(2022, 10, 28)
        self.testElem.save()

        tmp_elem = Item.objects.get(pk=self.testElem.pk)
        self.assertEqual(tmp_elem.date_exp, datetime(2022, 10, 28))

    def test_delete_item(self):
        nb_items_before_delete = Item.objects.count()
        self.testElem.delete()

        nb_items_after_delete = Item.objects.count()
        self.assertTrue(nb_items_after_delete == nb_items_before_delete - 1)



