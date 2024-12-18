from django.db import migrations

def create_sample_product(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Product.objects.create(
        name="Laptop",
        description="A high-performance laptop",
        price=1000.00,
        category="Electronics",
    )

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_product),
    ]
