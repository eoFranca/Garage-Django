# Generated by Django 5.0.6 on 2024-07-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_cor_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "Acessório", "verbose_name_plural": "Acessórios       "},
        ),
        migrations.AlterModelOptions(
            name="veiculo",
            options={"verbose_name": "Veículo", "verbose_name_plural": "Veículos"},
        ),
    ]
