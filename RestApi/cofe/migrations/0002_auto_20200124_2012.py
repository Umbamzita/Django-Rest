# Generated by Django 2.1 on 2020-01-24 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cofe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='s_drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cofe.Drink'),
        ),
    ]