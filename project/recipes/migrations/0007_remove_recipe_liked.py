# Generated by Django 3.0.4 on 2020-03-30 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='liked',
        ),
    ]
