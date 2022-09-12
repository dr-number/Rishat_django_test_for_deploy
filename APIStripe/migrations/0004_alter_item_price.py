# Generated by Django 4.1.1 on 2022-09-12 06:41

from unicodedata import name
from django.db import migrations, models

from APIStripe.models import Item


def add_poroduct(model, product_name, descr, cost):

    if not Item.objects.filter(name=product_name).exists():
        return model.objects.create(name=product_name, description=descr, price=cost)

    return True

def add_products_default(apps, schema_editor):

    model = apps.get_model("APIStripe", "Item")

    r1 = add_poroduct(model, "Mobile phone", "device 1", "150")
    r2 = add_poroduct(model, "PC", "device 2", "1500")
    r3 = add_poroduct(model, "Laptop", "device 3", "2000")

    result = r1 and r2 and r3

class Migration(migrations.Migration):

    dependencies = [
        ('APIStripe', '0003_remove_item_count_in_basked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),

        migrations.RunPython(add_products_default, reverse_code=migrations.RunPython.noop),
    ]