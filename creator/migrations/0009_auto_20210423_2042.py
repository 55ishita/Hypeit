# Generated by Django 3.1.7 on 2021-04-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0008_auto_20210423_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='cat1',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], default='None', max_length=70),
        ),
        migrations.AlterField(
            model_name='creator',
            name='cat2',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], default='None', max_length=70),
        ),
        migrations.AlterField(
            model_name='creator',
            name='cat3',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], default='None', max_length=70),
        ),
        migrations.AlterField(
            model_name='creator',
            name='cat4',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], default='None', max_length=70),
        ),
    ]