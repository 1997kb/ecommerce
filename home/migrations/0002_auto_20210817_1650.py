# Generated by Django 3.2.6 on 2021-08-17 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.brand', unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
