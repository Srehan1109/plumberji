# Generated by Django 3.2.14 on 2022-08-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_plumberprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plumberprofile',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]