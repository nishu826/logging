# Generated by Django 4.2 on 2023-04-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=10)),
                ('purchase_order', models.PositiveIntegerField()),
                ('mat_code', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('quantity', models.PositiveIntegerField()),
                ('qty_consumed', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('gate_pass', models.PositiveIntegerField()),
                ('Date',models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True))
            ],
        ),
    ]