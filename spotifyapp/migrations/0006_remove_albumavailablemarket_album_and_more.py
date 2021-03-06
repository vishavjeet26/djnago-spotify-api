# Generated by Django 4.0.5 on 2022-06-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyapp', '0005_remove_copyright_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumavailablemarket',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumavailablemarket',
            name='available_market',
        ),
        migrations.RemoveField(
            model_name='albumgenre',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumgenre',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='artistgenre',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='artistgenre',
            name='genre',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='genre',
            new_name='genres',
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(to='spotifyapp.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='available_markets',
            field=models.ManyToManyField(to='spotifyapp.availablemarket'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genres',
            field=models.ManyToManyField(to='spotifyapp.genre'),
        ),
        migrations.DeleteModel(
            name='AlbumArtist',
        ),
        migrations.DeleteModel(
            name='AlbumAvailableMarket',
        ),
        migrations.DeleteModel(
            name='AlbumGenre',
        ),
        migrations.DeleteModel(
            name='ArtistGenre',
        ),
    ]
