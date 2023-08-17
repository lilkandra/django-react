# Generated by Django 4.1.7 on 2023-07-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bag',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='backend.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
