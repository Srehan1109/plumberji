# Generated by Django 3.2.14 on 2022-07-20 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
    ]
