# Generated by Django 4.2 on 2024-05-16 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('lab', '0010_system_mouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.department'),
            preserve_default=False,
        ),
    ]
