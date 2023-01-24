# Generated by Django 3.2.14 on 2023-01-18 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=1000)),
                ('service_image', models.ImageField(upload_to='photos/service')),
                ('description', models.TextField(max_length=2000)),
                ('service_price', models.IntegerField()),
                ('slug', models.SlugField(max_length=500)),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.category')),
            ],
        ),
    ]
