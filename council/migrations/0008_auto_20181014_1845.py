# Generated by Django 2.1.2 on 2018-10-14 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0007_auto_20181014_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='council.Category'),
        ),
    ]