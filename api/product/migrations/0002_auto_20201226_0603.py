# Generated by Django 3.1.4 on 2020-12-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BF', 'උදේ'), ('LU', 'දවල්'), ('DI', 'රාත්\u200dරි'), ('SN', 'බයිට්'), ('BF-LU', 'උදේ-දවල්'), ('BF-DI', 'උදේ-රාත්\u200dරි'), ('LU-DI', 'දවල්-රාත්\u200dරි'), ('BF-LU-DI', 'උදේ-දවල්-රාත්\u200dරි')], max_length=50),
        ),
    ]
