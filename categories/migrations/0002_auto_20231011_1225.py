from django.db import migrations, models

def add_initial_data(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    Category.objects.create(name='Category A')
    Category.objects.create(name='Category B')

class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.RunPython(add_initial_data),
    ]
