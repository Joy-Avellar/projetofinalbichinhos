# Generated by Django 5.0.1 on 2024-01-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bichinhos', '0007_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(choices=[('GATO', 'Gato'), ('CACHORRO', 'Cachorro'), ('MACHO', 'Macho'), ('FEMEA', 'Fêmea')], default='', to='bichinhos.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
