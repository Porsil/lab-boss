# Generated by Django 3.2.16 on 2023-01-22 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workload',
            name='analyst',
            field=models.ForeignKey(limit_choices_to={'status': 'Active'}, on_delete=django.db.models.deletion.CASCADE, to='scheduler.analyst'),
        ),
        migrations.AlterField(
            model_name='workload',
            name='test',
            field=models.ForeignKey(limit_choices_to={'status': 'Active'}, on_delete=django.db.models.deletion.CASCADE, to='scheduler.test'),
        ),
    ]
