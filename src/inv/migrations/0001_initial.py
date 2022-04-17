# Generated by Django 3.1.6 on 2022-04-17 11:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(12), django.core.validators.MinLengthValidator(12)])),
                ('date_exp', models.DateField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.brand')),
            ],
        ),
    ]