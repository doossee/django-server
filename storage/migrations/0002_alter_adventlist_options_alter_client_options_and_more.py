# Generated by Django 4.2 on 2023-04-19 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adventlist',
            options={'ordering': ['-created_at'], 'verbose_name': 'Список приходов', 'verbose_name_plural': 'Списки приходов'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id'], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='consumptionlist',
            options={'ordering': ['-created_at'], 'verbose_name': 'Список расходов', 'verbose_name_plural': 'Списки расходов'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id', 'name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='profit',
            options={'ordering': ['-created_at'], 'verbose_name': 'Прибыль', 'verbose_name_plural': 'Прибыли'},
        ),
        migrations.AlterModelOptions(
            name='singleadvent',
            options={'ordering': ['id'], 'verbose_name': 'Приход', 'verbose_name_plural': 'Приходы'},
        ),
        migrations.AlterModelOptions(
            name='singleconsumption',
            options={'ordering': ['id'], 'verbose_name': 'Расход', 'verbose_name_plural': 'Расходы'},
        ),
    ]