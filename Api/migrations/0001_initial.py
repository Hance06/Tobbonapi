# Generated by Django 4.0.5 on 2022-06-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Belge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belge_basligi', models.CharField(max_length=200)),
                ('bagli_olunan_holding', models.CharField(max_length=200)),
                ('firma_unvani', models.CharField(max_length=200)),
                ('is_yeri_adresi', models.CharField(max_length=200)),
                ('merkezi_adres', models.CharField(max_length=200)),
                ('mersis_no', models.CharField(max_length=200)),
                ('sanayi_sicil_no', models.CharField(max_length=200)),
                ('tescilli_marka', models.CharField(max_length=200)),
                ('ticaret_sicil_no', models.CharField(max_length=200)),
                ('vergi_daire_no', models.CharField(max_length=200)),
                ('guncelleme_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
