# Generated by Django 4.0 on 2021-12-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
