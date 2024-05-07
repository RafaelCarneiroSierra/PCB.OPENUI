# Generated by Django 5.0.4 on 2024-05-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0009_gpu'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=16)),
                ('nome', models.CharField(max_length=16)),
                ('custo', models.FloatField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=16)),
                ('nome', models.CharField(max_length=16)),
                ('custo', models.FloatField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=16)),
                ('nome', models.CharField(max_length=16)),
                ('custo', models.FloatField()),
                ('preco', models.FloatField()),
            ],
        ),
    ]