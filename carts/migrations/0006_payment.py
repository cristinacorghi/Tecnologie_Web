# Generated by Django 3.2.3 on 2021-08-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=300)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]