# Generated by Django 4.0 on 2022-10-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_remove_post_picture_multimedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimedia',
            name='media',
            field=models.FileField(blank=True, upload_to='post_medias'),
        ),
    ]
