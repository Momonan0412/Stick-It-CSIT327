# Generated by Django 4.2.15 on 2024-09-21 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_board_privacy_settings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.ForeignKey(help_text='Choose Category', on_delete=django.db.models.deletion.CASCADE, to='website.category'),
        ),
        migrations.AlterField(
            model_name='board',
            name='privacy_settings',
            field=models.CharField(choices=[('PV', 'Private'), ('PB', 'Public')], help_text='Choose privacy', max_length=2),
        ),
    ]
