# Generated by Django 3.1.4 on 2021-03-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0002_auto_20210220_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utenti',
            old_name='NazioneUt',
            new_name='Email',
        ),
        migrations.AddField(
            model_name='utenti',
            name='NumTelefono',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]