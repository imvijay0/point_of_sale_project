# Generated by Django 5.1.7 on 2025-04-05 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pos_app.category'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
