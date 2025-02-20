# Generated by Django 3.0.4 on 2020-04-11 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_amount', models.IntegerField(default=0)),
                ('donator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
