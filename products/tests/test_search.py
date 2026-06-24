
from django.test import TestCase
from products.models import Product
from products.search_engine import search_rank
class T(TestCase):
    def test_priority(self):
        p=Product(product_name='Phone',product_description='x',category='Smartphones',tags='5g')
        self.assertGreater(search_rank([p],'smartphone')[0][0],0.89)
