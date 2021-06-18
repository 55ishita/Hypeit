# Generated by Django 3.1.7 on 2021-04-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210424_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_table',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='register_table',
            name='occupation',
        ),
        migrations.AddField(
            model_name='register_table',
            name='cat1',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='cat2',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='cat3',
            field=models.CharField(blank=True, choices=[('1', 'Fashion'), ('2', 'Food'), ('3', 'Music'), ('4', 'Art'), ('5', 'Lifestyle')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='facebook',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='register_table',
            name='instagram',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='register_table',
            name='snapchat',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='register_table',
            name='youtube',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=150),
        ),
    ]
