# Generated by Django 3.1.4 on 2021-01-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('BF', 'උදේ'), ('LU', 'දවල්'), ('DI', 'රාත්\u200dරි'), ('SN', 'බයිට්'), ('BF-LU', 'උදේ-දවල්'), ('BF-DI', 'උදේ-රාත්\u200dරි'), ('LU-DI', 'දවල්-රාත්\u200dරි'), ('BF-LU-DI', 'උදේ-දවල්-රාත්\u200dරි')], max_length=50)),
                ('is_stock_avalable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('category', models.CharField(choices=[('BF', 'උදේ'), ('LU', 'දවල්'), ('DI', 'රාත්\u200dරි')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('BF', 'උදේ'), ('LU', 'දවල්'), ('DI', 'රාත්\u200dරි'), ('SN', 'බයිට්'), ('BF-LU', 'උදේ-දවල්'), ('BF-DI', 'උදේ-රාත්\u200dරි'), ('LU-DI', 'දවල්-රාත්\u200dරි'), ('BF-LU-DI', 'උදේ-දවල්-රාත්\u200dරි')], max_length=50)),
                ('price', models.IntegerField()),
                ('is_stock_avalable', models.BooleanField(default=True)),
            ],
        ),
    ]