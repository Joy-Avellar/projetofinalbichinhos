# Generated by Django 5.0.1 on 2024-01-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('categoria', models.CharField(choices=[('', ''), ('GATO', 'Gato'), ('CACHORRO', 'Cachorro'), ('MACHO', 'Macho'), ('FEMEA', 'Fêmea')], default='', max_length=50)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(upload_to='fotos/%Y/%m/%d')),
                ('publicada', models.BooleanField(default=False)),
            ],
        ),
    ]
