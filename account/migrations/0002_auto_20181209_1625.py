# Generated by Django 2.0.7 on 2018-12-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='female',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='male',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(default=''),
        ),
    ]
