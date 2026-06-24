
from django.core.management.base import BaseCommand
from products.models import Product
import csv
class Command(BaseCommand):
    def add_arguments(self,p): p.add_argument('csvfile')
    def handle(self,*a,**o):
        with open(o['csvfile'],encoding='utf-8') as f:
            for r in csv.DictReader(f):
                Product.objects.create(**r)
