# Generated by Django 3.2.6 on 2021-08-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email адрес'),
        ),
    ]
