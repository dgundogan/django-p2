# Generated by Django 2.1.15 on 2020-03-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('score', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
