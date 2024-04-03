# Generated by Django 5.0.3 on 2024-04-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material_app', '0002_delete_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=255)),
                ('quantidade', models.IntegerField(default=0)),
                ('preco', models.FloatField(default=0)),
            ],
        ),
    ]
