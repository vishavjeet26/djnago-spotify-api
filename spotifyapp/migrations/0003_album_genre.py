# Generated by Django 4.0.5 on 2022-06-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyapp', '0002_alter_copyright_options_rename_label_copyright_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='spotifyapp.genre'),
        ),
    ]
