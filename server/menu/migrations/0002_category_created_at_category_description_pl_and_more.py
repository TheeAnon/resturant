# Generated by Django 5.0.6 on 2024-06-18 12:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='description_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pl',
            field=models.CharField(default='Polish', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='description_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name_pl',
            field=models.CharField(default='Polish', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
