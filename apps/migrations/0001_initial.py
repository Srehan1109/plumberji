# Generated by Django 3.2.14 on 2023-01-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000, unique=True)),
            ],
        ),
    ]
