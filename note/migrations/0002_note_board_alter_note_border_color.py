# Generated by Django 4.2.15 on 2024-11-26 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.board'),
        ),
        migrations.AlterField(
            model_name='note',
            name='border_color',
            field=models.CharField(max_length=100),
        ),
    ]
