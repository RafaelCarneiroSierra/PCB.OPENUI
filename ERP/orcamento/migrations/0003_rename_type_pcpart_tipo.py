# Generated by Django 5.0.5 on 2024-05-07 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0002_pcpart_delete_cpu_delete_gpu_delete_mob_delete_psu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pcpart',
            old_name='type',
            new_name='tipo',
        ),
    ]