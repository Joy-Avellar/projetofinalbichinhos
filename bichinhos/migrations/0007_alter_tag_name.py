# Generated by Django 5.0.1 on 2024-01-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bichinhos', '0006_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
